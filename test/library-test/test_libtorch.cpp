// Ref: https://github.com/prabhuomkar/pytorch-cpp/blob/master/tutorials/basics/pytorch_basics/main.cpp

#include <torch/torch.h>
#include <torch/script.h>
#include <iostream>


int main() {
    std::cout << "PyTorch Basics\n\n";

    // Set floating point output precision
    std::cout << std::fixed << std::setprecision(4);

    // === TODO: 1. BASIC AUTOGRAD EXAMPLE 1  
    std::cout << "---- BASIC AUTOGRAD EXAMPLE 1 ----\n";

    // Create Tensors
    torch::Tensor x = torch::tensor(1.0, torch::requires_grad());
    torch::Tensor w = torch::tensor(2.0, torch::requires_grad());
    torch::Tensor b = torch::tensor(3.0, torch::requires_grad());

    // Build a computational graph
    auto y = w * x + b;  // y = 2 * x + 3

    // Compute the gradients
    y.backward();

    // Print out the gradients
    std::cout << x.grad() << '\n';  // x.grad() = 2
    std::cout << w.grad() << '\n';  // w.grad() = 1
    std::cout << b.grad() << "\n\n";  // b.grad() = 1

    return 0;
}