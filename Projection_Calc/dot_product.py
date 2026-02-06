def solve_dot_product_2_vectors(VectorA, VectorB):
    print("\n-------------------- DOT PRODUCT --------------------")
    dot_product = 0
    products = []

    #Calculate individual products (dynamic)
    for i in range(len(VectorA)):
        product = VectorA[i] * VectorB[i]
        products.append(product)
        print(f"Element {i}: {VectorA[i]} * {VectorB[i]} = {product}")
        dot_product += product

    print(f"Dot Product: {dot_product}\n")
    return dot_product