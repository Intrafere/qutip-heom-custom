class BosonicBath:
    def __init__(self, gamma, lam, beta):
        self.gamma = gamma    # decay rate
        self.lam = lam        # reorganization energy
        self.beta = beta      # 1/(k_B * T)

    def spectral_density(self, omega):
        return 2 * self.lam * self.gamma * omega / (omega**2 + self.gamma**2)
