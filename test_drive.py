#/explain <file_name or method_name or any free text>


# Write a program that converts a Roman numeral to an integer

def roman_to_integer(s):
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    for char in reversed(s):
        value = roman_numerals[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    
    return total

print(roman_to_integer("XIV"))
print(roman_to_integer("LVIII"))
print(roman_to_integer("MCMXCIV"))

# Write a program that calculates the factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(factorial(5))  # Output: 120
print(factorial(0))  # Output: 1


# Write a program that generates a blog
def generate_blog(title, content):
    blog_template = f"""
    <html>
    <head>
        <title>{title}</title>
    </head>
    <body>
        <h1>{title}</h1>
        <p>{content}</p>
    </body>
    </html>
    """
    return blog_template

blog_title = "My First Blog"
blog_content = "This is the content of my first blog post."
print(generate_blog(blog_title, blog_content))