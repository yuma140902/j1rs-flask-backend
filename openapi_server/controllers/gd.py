import numpy as np


def get_loss_function(f):
    def loss_function(xs, ys, params):
        N = len(xs)
        sum_error = 0.0
        for i in range(N):
            sum_error += (ys[i] - f(xs[i], params)) ** 2.0
        return sum_error / float(N)
    return loss_function


def partial_diff(loss_function, xs, ys, h=1e-8):
    def d(i, params):
        d_params = np.zeros_like(params)
        d_params[i] = h / 2.0
        return (loss_function(xs, ys, params + d_params) -
                loss_function(xs, ys, params - d_params)) / h
    return d


def gradient_descent(xs,
                     ys,
                     loss_function,
                     learning_rate,
                     initial_params,
                     convergence_epsillon,
                     MAX_ITER=1000):
    params = initial_params
    d_loss_function = partial_diff(loss_function, xs, ys)
    gradients = np.zeros_like(params)
    num_iter = 0

    while True:
        num_iter += 1

        # 勾配を計算する
        for i in range(len(gradients)):
            gradients[i] = d_loss_function(i, params)

        # パラメータを更新する
        for i in range(len(gradients)):
            params[i] = params[i] - learning_rate * gradients[i]

        loss = loss_function(xs, ys, params)

        params_str = ", ".join([f'{p:.5f}' for p in params])
        print(f'[{num_iter:3d}] loss={loss:.10f}, params={params_str}')

        if loss <= convergence_epsillon:
            print(f"break because {loss} <= {convergence_epsillon}")
            break

        if num_iter >= MAX_ITER:
            print("maximum num_iter")
            break
    return params


if __name__ == '__main__':
    initial_params = [2.0, 3.0]
    xs = np.arange(0, 10, 0.5)
    ys = xs * 3 + 1

    def f(x, p):
        return p[0] * x + p[1]

    loss_function = get_loss_function(f)
    print(gradient_descent(xs, ys, loss_function, 0.01, initial_params, 1e-4))
