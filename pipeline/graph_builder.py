import pandas as pd
import networkx as nx

def build_transaction_graph(transactions: pd.DataFrame) -> nx.Graph:
    """
    Build a graph where nodes are accounts and edges are transactions.
    """
    G = nx.Graph()
    for _, row in transactions.iterrows():
        src, dst, amount = row['src'], row['dst'], row['amount']
        G.add_edge(src, dst, weight=amount)
    return G
