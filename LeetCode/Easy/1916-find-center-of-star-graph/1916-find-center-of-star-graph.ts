function findCenter(edges: number[][]): number {
    const [first, second]=edges[0];
    const firstResult = edges.find(e=>!e.includes(first))

    return firstResult ? second : first;
};