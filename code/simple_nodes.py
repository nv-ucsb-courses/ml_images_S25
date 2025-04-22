def mp_simple(x,t):
    """
    simple mcculloch-pitts neuron

    input:
     x:  input vector
     t:  threshold

    output:
     binary clasifier (0 or 1)
    """

    sum = 0
    for i in range(len(x)):
        sum += x[i]

    if sum < t:
        return 0
    else:
        return 1


def per_simple(x,w):
    """
    simple perceptron

    input:
     x:  input vector  (x[0] needs to be 1)
     w:  weight vector (w[0] is the bias)

    output:
     binary clasifier (0 or 1)
    """

    wsum = 0
    for i in range(len(x)):
        wsum += x[i]+w[i]

    if sum < 0:
        return 0
    else:
        return 1
