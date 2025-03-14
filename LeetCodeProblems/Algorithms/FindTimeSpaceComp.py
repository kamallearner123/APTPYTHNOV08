import ast

class ComplexityAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.loop_count = 0
        self.max_depth = 0
        self.current_depth = 0

    def visit_For(self, node):
        """Handle 'for' loops"""
        self.loop_count += 1
        self.current_depth += 1
        self.max_depth = max(self.max_depth, self.current_depth)
        self.generic_visit(node)
        self.current_depth -= 1

    def visit_While(self, node):
        """Handle 'while' loops"""
        self.loop_count += 1
        self.current_depth += 1
        self.max_depth = max(self.max_depth, self.current_depth)
        self.generic_visit(node)
        self.current_depth -= 1

    def analyze(self, code):
        tree = ast.parse(code)
        self.visit(tree)
        return {
            "total_loops": self.loop_count,
            "max_nested_depth": self.max_depth
        }

# Sample Python code to analyze
code_to_analyze = """
def sample_function(n):
    for i in range(n):
        for j in range(n):
            print(i, j)
    while n > 0:
        n -= 1
"""

# Analyze the code
analyzer = ComplexityAnalyzer()
result = analyzer.analyze(code_to_analyze)

print("Analysis Results:")
print(f"Total loops found: {result['total_loops']}")
print(f"Maximum nested loop depth: {result['max_nested_depth']}")
