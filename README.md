# AI/ML Learning Log

A first-principles journey through Artificial Intelligence and Machine
Learning.

This repository documents my progress while learning ML by
**understanding and implementing the core ideas myself**, rather than
jumping directly into high-level frameworks.

The goal is not just to make models work, but to understand **why they
work**.

------------------------------------------------------------------------

## 🎯 Goal

Build strong foundations in:

-   Machine Learning fundamentals
-   Mathematics behind ML
-   Neural networks
-   Deep learning
-   Model training and optimization
-   NumPy-based implementations
-   Eventually PyTorch and modern deep learning systems

The long-term goal is to become capable of going from:

> **Mathematical idea → implementation → experiment → working model**

------------------------------------------------------------------------

## 🧭 Learning Philosophy

I am following a **first-principles approach**.

For every new concept, I try to understand:

1.  **What is it?**
2.  **Why do we need it?**
3.  **How does it work?**
4.  **What mathematics produces the result?**
5.  **How does that mathematics become code?**
6.  **What happens when we actually run it?**

I am deliberately avoiding treating ML as a collection of formulas to
memorize.

------------------------------------------------------------------------

# 📚 Current Learning Path

``` text
Python
   ↓
NumPy
   ↓
Linear Regression from Scratch
   ↓
Logistic Regression from Scratch
   ↓
Neural Networks from Scratch
   ↓
MNIST from Scratch
   ↓
Karpathy — Zero to Hero
   ↓
PyTorch / Autograd
   ↓
More Advanced Deep Learning
   ↓
MIT 15.773 / Advanced DL
   ↓
ML Theory / Stanford CS229
```

This roadmap will evolve as my understanding improves.

------------------------------------------------------------------------

# ✅ Progress

## 1. Python

### Covered

-   Variables and data types
-   Strings
-   Numbers
-   Lists
-   Tuples
-   Dictionaries
-   Conditions
-   Loops
-   Functions
-   Return values
-   File handling
-   Exceptions
-   Modules and pip
-   Basic classes and objects

Python is being treated mainly as the language needed to implement ML
ideas.

------------------------------------------------------------------------

## 2. NumPy

### Covered

-   Arrays
-   Array shape
-   `ndim`
-   Indexing
-   Slicing
-   Reshaping
-   Transpose
-   Broadcasting
-   Element-wise operations
-   Boolean masking
-   Random initialization
-   Statistics
-   Matrix operations
-   Dot products
-   Vectorization

NumPy is currently the main tool for understanding what higher-level ML
frameworks do internally.

------------------------------------------------------------------------

# 🧠 Machine Learning Implementations

## Linear Regression --- From Scratch

Implemented using NumPy.

### Concepts learned

-   Parameters
-   Weight
-   Bias
-   Prediction
-   Mean Squared Error
-   Derivatives
-   Gradients
-   Learning rate
-   Gradient descent
-   Epochs
-   Training loops

### Core model

``` text
ŷ = XW + b
```

### Training process

``` text
Data
 ↓
Prediction
 ↓
Loss
 ↓
Gradient
 ↓
Parameter Update
 ↓
Repeat
```

------------------------------------------------------------------------

# Logistic Regression --- From Scratch

Implemented using NumPy.

### Concepts learned

-   Binary classification
-   Sigmoid
-   Probability-like outputs
-   Decision thresholds
-   Binary Cross-Entropy
-   Derivatives
-   Chain rule
-   Gradient descent

### Sigmoid

``` text
σ(z) = 1 / (1 + e^(-z))
```

### Core training idea

``` text
X
 ↓
z = XW + b
 ↓
Sigmoid
 ↓
Probability
 ↓
BCE Loss
 ↓
Gradient
 ↓
Update W and b
```

An important result encountered:

``` text
dL/dz = ŷ - y
```

This is where the mathematics started connecting directly to the
implementation.

------------------------------------------------------------------------

# Neural Networks --- From Scratch

Built a small two-layer neural network using only NumPy.

## Architecture

``` text
Input
784 pixels
   ↓
Dense Layer
784 → 128
   ↓
ReLU
   ↓
Dense Layer
128 → 10
   ↓
Softmax
   ↓
10 class probabilities
```

### Concepts learned

-   Neurons
-   Weights
-   Biases
-   Dense layers
-   Matrix multiplication
-   ReLU
-   Softmax
-   Cross-entropy
-   Forward propagation
-   Backpropagation
-   Gradients
-   Chain rule
-   Mini-batches
-   Epochs
-   Gradient descent

------------------------------------------------------------------------

# 🔢 MNIST --- From Scratch

MNIST is currently the main practical project in this learning phase.

### Dataset

``` text
Training: 60,000 images
Testing:  10,000 images

Each image:
28 × 28 pixels
= 784 input values
```

### Preprocessing

``` python
X = image.reshape(1, 784) / 255.0
```

This converts the image from:

``` text
28 × 28
```

into:

``` text
784
```

and scales pixel values from approximately:

``` text
0–255
```

to:

``` text
0–1
```

------------------------------------------------------------------------

# 🔬 MNIST Network

## Layer 1

``` text
784 → 128
```

``` python
Z1 = X @ W1 + b1
A1 = np.maximum(0, Z1)
```

## Layer 2

``` text
128 → 10
```

``` python
Z2 = A1 @ W2 + b2
```

## Output

``` python
probabilities = softmax(Z2)
```

The ten outputs correspond to:

``` text
0 1 2 3 4 5 6 7 8 9
```

------------------------------------------------------------------------

# 🔙 Backpropagation

One of the most important concepts encountered so far.

The network follows:

``` text
Forward:

X
 ↓
Z1
 ↓
A1
 ↓
Z2
 ↓
Prediction
 ↓
Loss
```

Then backpropagation reverses the dependency:

``` text
Loss
 ↓
dZ2
 ↓
dW2, db2
 ↓
dA1
 ↓
dZ1
 ↓
dW1, db1
```

The central mathematical idea is the **chain rule**.

Backpropagation is being learned as:

> Applying the chain rule systematically through the computational
> graph.

------------------------------------------------------------------------

# 📦 Mini-Batch Training

Instead of processing all 60,000 images at once, the network currently
uses:

``` text
Batch size = 32
```

Therefore:

``` text
60,000 / 32 = 1,875 batches
```

One epoch means processing all 1,875 batches once.

Each batch performs:

``` text
Forward
 ↓
Loss
 ↓
Backward
 ↓
Update
```

------------------------------------------------------------------------

# 📈 Current MNIST Result

The network was trained for 5 epochs.

Example training losses:

``` text
Epoch 1 → 1.2559
Epoch 2 → 0.4316
Epoch 3 → 0.3490
Epoch 4 → 0.3140
Epoch 5 → 0.2896
```

The model also correctly classified an unseen test image:

``` text
Actual:    7
Predicted: 7
```

with approximately:

``` text
P(7) = 0.996
```

This is only a single-image test so far; full test-set accuracy is the
next evaluation step.

------------------------------------------------------------------------

# 📐 Mathematics Encountered

The mathematics is being learned **through the implementations**, rather
than as a separate abstract subject.

### Algebra

``` text
ŷ = wx + b
```

### Summations and averages

``` text
(1/N) Σ
```

### Exponentials

Used in:

``` text
Sigmoid
Softmax
```

### Logarithms

Used in:

``` text
Cross-Entropy
```

### Derivatives

Used to determine:

``` text
How does the loss change when a parameter changes?
```

### Partial derivatives

``` text
∂L/∂W
∂L/∂b
```

### Chain rule

Used to connect:

``` text
Parameter → intermediate value → prediction → loss
```

### Matrix multiplication

``` text
X @ W
```

### Transpose

``` text
X.T
```

### Gradients

A collection of derivatives used to determine parameter updates.

### Gradient descent

``` text
parameter ← parameter − learning_rate × gradient
```

### Probability

Used in:

``` text
Sigmoid
Softmax
Classification
```

A separate mathematics reference is maintained alongside this
repository.

------------------------------------------------------------------------

# 🗂️ Repository Structure

The structure will evolve as the learning journey grows.

A possible structure is:

``` text
ai-ml-log/
│
├── README.md
│
├── python/
│
├── numpy/
│
├── linear_regression/
│
├── logistic_regression/
│
├── neural_network/
│
├── mnist/
│   ├── MNIST_Neural_Network_From_Scratch_NumPy.ipynb
│   └── ...
│
├── notes/
│   └── ...
│
└── resources/
    └── ...
```

The exact structure may change as projects become larger.

------------------------------------------------------------------------

# 🧪 Experiments

This repository is also a record of experiments.

Not everything here is expected to be polished.

Some notebooks may contain:

-   Failed experiments
-   Debugging
-   Different learning rates
-   Shape mistakes
-   Incorrect implementations
-   Intermediate experiments
-   Comparisons between approaches

The goal is to preserve the **learning process**, not just the final
answer.

------------------------------------------------------------------------

# 🚀 Upcoming

### Immediate

-   Evaluate MNIST on all 10,000 test images
-   Calculate test accuracy
-   Inspect incorrect predictions
-   Visualize predictions
-   Understand why some digits are misclassified

### Next

-   Improve the NumPy neural network
-   Experiment with architecture
-   Understand initialization more deeply
-   Understand optimization better
-   Implement more models from scratch

### Then

-   Karpathy's **Zero to Hero**
-   Automatic differentiation
-   PyTorch
-   More advanced neural networks
-   Larger datasets
-   More serious ML projects

------------------------------------------------------------------------

# 🛠️ Environment

Current development environment:

``` text
Python 3.12
NumPy
Matplotlib
Jupyter
TensorFlow
```

TensorFlow is currently used primarily for convenient MNIST dataset
loading, while the neural network itself is implemented manually with
NumPy.

------------------------------------------------------------------------

# 📖 Learning Resources

Current / planned resources include:

-   NumPy documentation
-   Karpathy --- Zero to Hero
-   MIT 15.773 --- Hands-On Deep Learning
-   Stanford ML / CS229
-   Official PyTorch documentation

------------------------------------------------------------------------

# 🧠 Core Principle

The main principle of this repository is:

``` text
Don't just use the abstraction.

Understand what the abstraction is doing.
```

For example, instead of immediately writing:

``` python
model.fit(X, y)
```

the goal is to first understand what happens underneath:

``` text
Prediction
    ↓
Loss
    ↓
Derivative
    ↓
Backpropagation
    ↓
Gradient
    ↓
Parameter update
```

Eventually, frameworks such as PyTorch become tools rather than black
boxes.

------------------------------------------------------------------------

## Progress Log

This README will be updated as new concepts, implementations,
experiments, and projects are completed.

> **Learning ML from the inside out.**
