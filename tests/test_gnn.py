import torch
from torch_geometric.data import Data
from models.gnn import FraudGNN

def test_gnn_forward_pass():
    # Dummy graph: 3 nodes, 2 edges
    x = torch.rand((3, 4))  # 3 nodes, 4 features
    edge_index = torch.tensor([[0, 1], [1, 2]], dtype=torch.long).t().contiguous()

    model = FraudGNN(in_channels=4, hidden_channels=8, out_channels=2)
    out = model(x, edge_index)

    assert out.shape == (3, 2)  # 3 nodes, 2 output classes
