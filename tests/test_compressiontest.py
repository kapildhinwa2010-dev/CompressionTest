import pytest
import torch
from compressiontest import CompressionTest, create_compressiontest

class TestCompressionTest:
    def test_init(self):
        m = CompressionTest(dim=256, hidden_dim=512)
        assert m.dim == 256
    
    def test_forward(self):
        m = CompressionTest(dim=256)
        x = torch.randn(32, 256)
        assert m(x).shape == (32, 256)
    
    def test_factory(self):
        m = create_compressiontest()
        assert isinstance(m, CompressionTest)

if __name__ == '__main__':
    pytest.main([__file__, '-v'])
