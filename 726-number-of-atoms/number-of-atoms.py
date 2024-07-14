class Solution:
    def countOfAtoms(self, formula: str) -> str:
        # Stack to hold the current level of counts
        stack = [Counter()]
        i = 0
        n = len(formula)
        
        while i < n:
            if formula[i] == '(':
                # Start a new level of counts
                stack.append(Counter())
                i += 1
            elif formula[i] == ')':
                # End the current level of counts
                i += 1
                # Find the multiplier
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                multiplier = int(formula[start:i] or 1)
                # Pop the current level and merge it into the previous level
                top = stack.pop()
                for elem, count in top.items():
                    stack[-1][elem] += count * multiplier
            else:
                # Read the element name
                start = i
                i += 1
                while i < n and formula[i].islower():
                    i += 1
                elem = formula[start:i]
                # Read the number
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                count = int(formula[start:i] or 1)
                # Add the count to the current level
                stack[-1][elem] += count
        
        # The final counts are in the last item on the stack
        result = stack.pop()
        # Sort by element names
        sorted_elements = sorted(result.items())
        # Build the output string
        output = []
        for elem, count in sorted_elements:
            output.append(elem)
            if count > 1:
                output.append(str(count))
        
        return ''.join(output)
        