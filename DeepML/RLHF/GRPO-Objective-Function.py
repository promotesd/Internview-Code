import numpy as np

def grpo_objective(rhos, A, pi_theta_old, pi_theta_ref, epsilon=0.2, beta=0.01) -> float:

    rhos=np.array(rhos)
    A=np.array(A)
    pi_theta_old=np.array(pi_theta_old)
    pi_theta_ref=np.array(pi_theta_ref)

    if not len(A)==len(rhos)==len(pi_theta_old)==len(pi_theta_ref):
        raise ValueError("All input lists must have the same length")

    ratio=rhos*A
    rhos_clip=np.clip(rhos, 1-epsilon, 1+epsilon)
    ratio_clip=rhos_clip*A
    min_term=np.minimum(ratio, ratio_clip)

    pi_theta=rhos*pi_theta_old
    pi_theta=np.maximum(pi_theta, 1e-10)
    pi_theta_ref=np.maximum(pi_theta_ref, 1e-10)

    Dkl=(pi_theta_ref/pi_theta)-np.log(pi_theta_ref/pi_theta)-1
    J=np.mean(min_term-beta*Dkl)
    return J

    