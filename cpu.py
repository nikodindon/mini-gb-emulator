# cpu.py
class CPU:
    def __init__(self):
        # registres A, B, C, D, E, H, L, F
        self.A = 0
        self.B = 0
        self.C = 0
        self.D = 0
        self.E = 0
        self.H = 0
        self.L = 0
        self.F = 0  # flags

    def dump_registers(self):
        print(f"A={self.A} B={self.B} C={self.C} D={self.D} E={self.E} H={self.H} L={self.L} F={self.F}")


if __name__ == "__main__":
    cpu = CPU()
    cpu.dump_registers()