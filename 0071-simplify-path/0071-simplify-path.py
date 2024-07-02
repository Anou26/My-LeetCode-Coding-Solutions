class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        # Initialize a stack to keep the valid directory names
        stack = []
        
        # Split the input path by '/'
        components = path.split('/')
        
        for component in components:
            # If the component is '..', pop from stack if it is not empty
            if component == '..':
                if stack:
                    stack.pop()
            # If the component is valid (not empty or '.'), push it onto the stack
            elif component and component != '.':
                stack.append(component)
        
        # Join the components in the stack to form the simplified path
        return '/' + '/'.join(stack)

# Example usage:
# solution = Solution()
# print(solution.simplifyPath("/home/")) # Output: "/home"
# print(solution.simplifyPath("/home//foo/")) # Output: "/home/foo"
# print(solution.simplifyPath("/home/user/Documents/../Pictures")) # Output: "/home/user/Pictures"
# print(solution.simplifyPath("/../")) # Output: "/"
# print(solution.simplifyPath("/.../a/../b/c/../d/./")) # Output: "/.../b/d"
