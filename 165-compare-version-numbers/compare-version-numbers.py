class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        def normalize(version):
            return [int(part) for part in version.split(".")]

        v1 = normalize(version1)
        v2 = normalize(version2)

        max_len = max(len(v1), len(v2))

        v1 += [0] * (max_len - len(v1))
        v2 += [0] * (max_len - len(v2))

        for part1, part2 in zip(v1, v2):
            if part1 < part2:
                return -1
            elif part1 > part2:
                return 1

        return 0
        '''
        parts1 = version1.split(".")  # Split the number by periods
        filtered_parts = [part for part in parts1 if part != "0"]  # Remove zero parts
        modified_number1 = ".".join(filtered_parts)
        
        parts2 = version2.split(".")  # Split the number by periods
        filtered_parts2 = [part for part in parts2 if part != "0"]  # Remove zero parts
        modified_number2 = ".".join(filtered_parts2)
        print(modified_number1,modified_number2)

        if modified_number1 > modified_number2:
            return 1
        elif modified_number1 < modified_number2:
            return -1
        else:
            return 0
'''