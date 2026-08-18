import math
import streamlit as st

# escalaaaaaaa
CHEESES = [
    {"name": "Brie", "scores": {"cremosidade": 5, "intensidade": 2, "sal": 2, "acidez": 1, "maturacao": 1}},
    {"name": "Gorgonzola", "scores": {"cremosidade": 3, "intensidade": 5, "sal": 4, "acidez": 2, "maturacao": 4}},
    {"name": "Parmesão", "scores": {"cremosidade": 1, "intensidade": 4, "sal": 4, "acidez": 3, "maturacao": 5}},
    {"name": "Gouda", "scores": {"cremosidade": 3, "intensidade": 3, "sal": 2, "acidez": 1, "maturacao": 2}},
    {"name": "Mussarela de Búfala", "scores": {"cremosidade": 4, "intensidade": 1, "sal": 1, "acidez": 2, "maturacao": 1}},
    {"name": "Roquefort", "scores": {"cremosidade": 4, "intensidade": 5, "sal": 5, "acidez": 2, "maturacao": 4}},
    {"name": "Camembert", "scores": {"cremosidade": 5, "intensidade": 3, "sal": 2, "acidez": 1, "maturacao": 2}},
    {"name": "Gruyère", "scores": {"cremosidade": 3, "intensidade": 3, "sal": 3, "acidez": 4, "maturacao": 3}},
    {"name": "Provolone", "scores": {"cremosidade": 2, "intensidade": 4, "sal": 3, "acidez": 2, "maturacao": 3}},
    {"name": "Feta", "scores": {"cremosidade": 2, "intensidade": 3, "sal": 5, "acidez": 1, "maturacao": 1}},
    {"name": "Ricota", "scores": {"cremosidade": 4, "intensidade": 1, "sal": 1, "acidez": 1, "maturacao": 1}},
    {"name": "Queijo Prato", "scores": {"cremosidade": 4, "intensidade": 2, "sal": 2, "acidez": 2, "maturacao": 2}},
    {"name": "Emmental", "scores": {"cremosidade": 3, "intensidade": 2, "sal": 2, "acidez": 2, "maturacao": 3}},
    {"name": "Queijo Coalho", "scores": {"cremosidade": 2, "intensidade": 3, "sal": 4, "acidez": 2, "maturacao": 2}},
    {"name": "Camembert", "scores": {"cremosidade": 5, "intensidade": 4, "sal": 3, "acidez": 2, "maturacao": 2}},
    {"name": "Queijo de Cabra", "scores": {"cremosidade": 4, "intensidade": 4, "sal": 3, "acidez": 5, "maturacao": 1}},
    {"name": "Cheddar", "scores": {"cremosidade": 3, "intensidade": 4, "sal": 4, "acidez": 3, "maturacao": 3}}
]

#pratos favs
FOOD_PROFILES = {
    "Pizza de Pepperoni": {"cremosidade": 2, "intensidade": 4, "sal": 4, "acidez": 2, "maturacao": 3},
    "Mac and Cheese": {"cremosidade": 5, "intensidade": 3, "sal": 3, "acidez": 1, "maturacao": 2},
    "Salada Grega": {"cremosidade": 2, "intensidade": 3, "sal": 5, "acidez": 4, "maturacao": 1},
    "Lasanha Bolognesa": {"cremosidade": 4, "intensidade": 4, "sal": 3, "acidez": 2, "maturacao": 3},
    "Hamburguer Artesanal": {"cremosidade": 3, "intensidade": 4, "sal": 3, "acidez": 2, "maturacao": 3},
    "Massa ao Molho Quatro Queijos": {"cremosidade": 5, "intensidade": 4, "sal": 4, "acidez": 1, "maturacao": 4},
    "Tacos/Burritos": {"cremosidade": 3, "intensidade": 5, "sal": 4, "acidez": 4, "maturacao": 2},
    "Sanduíche na Chapa": {"cremosidade": 3, "intensidade": 2, "sal": 3, "acidez": 1, "maturacao": 1}
}

#algoritmo
def recommend_cheese(user_selected_foods):
    user_vector = {"cremosidade": 0, "intensidade": 0, "sal": 0, "acidez": 0, "maturacao": 0}
    for food in user_selected_foods:
        for key in user_vector:
            user_vector[key] += FOOD_PROFILES[food][key] / len(user_selected_foods)
    max_distance = math.sqrt(5 *(4 ** 2))
    results = []
    for cheese in CHEESES:
        distance = math.sqrt(
            sum((user_vector[attr] - cheese["scores"][attr]) ** 2 for attr in user_vector)
        )
        match_percentage = round((1 - (distance / max_distance)) * 100, 1)
        results.append({"cheese": cheese["name"], "match": match_percentage})
    return sorted(results, key=lambda x: x["match"], reverse=True)

st.set_page_config(page_title="Recomendador de Queijos")
st.title("Recomendador Inteligentes de Queijos")
st. write("Selecione os seus pratos favoritos e descubra quais queijos combinam com o seu paladar!")
pratos_selecionados = st.multiselect(
    "Escolha um ou mais pratos:",
    options=list(FOOD_PROFILES.keys()),
    default=["Pizza de Pepperoni"]
)
if st.button("Gerar Recomendação") and pratos_selecionados:
    recomendacoes = recommend_cheese(pratos_selecionados)
    st.markdown("---")
    st.subheader("Queijos recomendados para si:")
    for rec in recomendacoes[:3]:
        st.write(f"**{rec['cheese']}** - {rec['match']}% de compatibilidade")
        st.progress(int(rec['match']))