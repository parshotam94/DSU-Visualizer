from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

# Grid Configuration
ROWS, COLS = 20, 20
grid = ["#ffffff"] * (ROWS * COLS)

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i]) # Path Compression
        return self.parent[i]

    def unite(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            # Union by Size
            if self.size[root_i] < self.size[root_j]:
                root_i, root_j = root_j, root_i
            self.parent[root_j] = root_i
            self.size[root_i] += self.size[root_j]
            return True
        return False

def calculate_clusters():
    dsu = DSU(ROWS * COLS)
    # Connect adjacent pixels of the same color
    for r in range(ROWS):
        for c in range(COLS):
            idx = r * COLS + c
            # Check Right
            if c + 1 < COLS and grid[idx] == grid[idx + 1] and grid[idx] != "#ffffff":
                dsu.unite(idx, idx + 1)
            # Check Down
            if r + 1 < ROWS and grid[idx] == grid[idx + COLS] and grid[idx] != "#ffffff":
                dsu.unite(idx, idx + COLS)
    
    # Count unique roots (excluding white background)
    clusters = set()
    for i in range(ROWS * COLS):
        if grid[i] != "#ffffff":
            clusters.add(dsu.find(i))
    return len(clusters)

@app.route('/')
def index():
    return render_template('index.html', rows=ROWS, cols=COLS)

@socketio.on('pixel_update')
def handle_pixel(data):
    idx = data['index']
    grid[idx] = data['color']
    count = calculate_clusters()
    emit('update_grid', {'index': idx, 'color': data['color'], 'cluster_count': count}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)