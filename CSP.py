class CSP:
    def __init__(self, variables, Domains, constraints):
        self.variables = variables
        self.domains = Domains
        self.constraints = constraints
        self.solution = None
        self.assignment = {}

    def solve(self):
        self.solution = self.backtrack()
        return self.solution

    def backtrack(self):
        if len(self.assignment) == len(self.variables):
            return self.assignment
        var = self.select_unassigned_variable()
        for value in self.order_domain_values(var):
            if self.is_consistent(var, value):
                self.assignment[var] = value
                result = self.backtrack()
                if result is not None:
                    return result
                del self.assignment[var]
        return None

    def select_unassigned_variable(self):
        unassigned_vars = [var for var in self.variables]
        for var in self.assignment:
            unassigned_vars.remove(var)
        return min(unassigned_vars, key=lambda var: len(self.domains[var]))

    def order_domain_values(self, var):
        return self.domains[var]

    def is_consistent(self, var, value):
        for constraint_var in self.constraints[var]:
            if constraint_var in self.assignment and self.assignment[constraint_var] == value:
                return False
        return True

