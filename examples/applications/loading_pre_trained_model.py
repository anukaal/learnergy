import torch
import torchvision
from learnergy.models.rbm import RBM
from torch.utils.data import DataLoader

if __name__ == '__main__':
    # Creating testing dataset
    test = torchvision.datasets.MNIST(
        root='./data', train=False, download=True, transform=torchvision.transforms.ToTensor())

    # Creating testing batches
    test_batches = DataLoader(test, batch_size=10000,
                              shuffle=True, num_workers=1)

    # Loading pre-trained model
    model = torch.load('model.pth')

    # Reconstructing test set
    rec_mse, v = model.reconstruct(test_batches)
