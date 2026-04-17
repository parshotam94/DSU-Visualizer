
# 🌐 PixelClan: Real-Time Cluster Analyzer

**PixelClan** is a real-time, collaborative grid-based application that demonstrates the power of the **Disjoint Set Union (DSU)** data structure. As multiple users paint on a shared canvas, the system dynamically calculates the number of distinct "territories" (connected components of the same color) using high-performance grouping algorithms.



## 🚀 The Core Challenge
In a real-time grid, calculating how many unique shapes exist after every single pixel update is computationally expensive. 
* **The Naive Way:** Running a Breadth-First Search (BFS) or DFS across the entire grid every time a pixel changes. Complexity: $O(N \times M)$ per click.
* **The DSU Way (Used here):** Only checking the immediate neighbors of the updated pixel and "uniting" sets. Complexity: Nearly $O(1)$ per click thanks to the **Inverse Ackermann Function** $\alpha(n)$.

---

## 🛠️ Features
* **Real-Time Collaboration:** Powered by **WebSockets (Socket.io)** for instant synchronization across all connected clients.
* **Dynamic Connectivity:** Uses DSU with **Path Compression** and **Union by Size** to merge clusters instantly.
* **Live Analytics:** A dashboard showing the total count of active "Territories" on the map.
* **Educational Console:** A frontend log that explains the DSU operations (`Find` and `Unite`) occurring in the background.

---

## 🧠 Data Structure Implementation
The project implements DSU with two critical optimizations that ensure it scales even to massive grids:

1.  **Path Compression:** During the `find` operation, every node visited is attached directly to the root, flattening the structure for future queries.
2.  **Union by Size/Rank:** When merging two sets, the smaller tree is always added under the larger tree, preventing the formation of deep, inefficient chains.



---

## 💻 Tech Stack
* **Frontend:** HTML5, CSS3, JavaScript (ES6+)
* **Backend:** Python / Flask
* **Real-Time:** Flask-SocketIO (WebSockets)
* **Algorithm Logic:** Disjoint Set Union (C++ logic mirrored in Python for seamless Flask integration)

---

## 🏃 Setup & Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/pixel-dsu-analyzer.git
    cd pixel-dsu-analyzer
    ```

2.  **Install dependencies:**
    ```bash
    pip install flask flask-socketio
    ```

3.  **Run the server:**
    ```bash
    python app.py
    ```

4.  **Explore:**
    Open `http://localhost:5000` in multiple browser tabs to see the real-time merging of sets in action!

---

## 📈 Future Roadmap
* **WebAssembly Engine:** Porting the DSU logic to C++ compiled via WASM for even faster client-side processing.
* **Snapshot Persistence:** Saving the grid state to a Redis database to maintain clusters after a server restart.
* **Heatmaps:** Visualizing which "Ultimate Leaders" (roots) have the most pixels under their command.
