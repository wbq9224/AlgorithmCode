import numpy as np


def conv_forward_pass(x, w, b, conv_param):
    N, C, H, W = x.shape
    F, _, HH, WW = w.shape

    S = conv_param['stride']
    P = conv_param['padding']

    HO = int(1 + (H + 2 * P - HH) / S)
    WO = int(1 + (W + 2 * P - WW) / S)

    x_pad = np.zeros((N, C, H + 2 * P, W + 2 * P))
    x_pad[:, :, P: P + H, P: P + W] = x

    out = np.zeros((N, F, HO, WO))

    for f in range(F):
        for i in range(HO):
            for j in range(WO):
                out[:, f, i, j] = np.sum(x_pad[:, :, i * S: i * S + HH, j * S: j * S + WW] * w[f, :, :, :], axis=(1, 2, 3))

        out[:, f, :, :] += b[f]

    cache = (x, w, b, conv_param)
    return out, cache


if __name__ == '__main__':
    x_shape = (2, 3, 4, 4)  # n,c,h,w
    w_shape = (2, 3, 3, 3)  # f,c,hw,ww
    x = np.ones(x_shape)
    w = np.ones(w_shape)
    b = np.array([1, 2])

    conv_param = {'stride': 1, 'padding': 0}
    out, _ = conv_forward_pass(x, w, b, conv_param)

    print(out)
    print(out.shape)