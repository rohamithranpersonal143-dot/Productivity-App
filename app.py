import random
import streamlit as st

# Setup page title and mobile-friendly layout
st.set_page_config(page_title="My Daily Tool", page_icon="🏃‍♂️", layout="centered")

st.title("📱 My Everyday Assistant")
st.write("---")

# ==========================================
# TOOL 1: STEPS GOAL RANDOMIZER
# ==========================================
st.header("🏃‍♂️ Daily Steps Randomizer")
st.write("Set your custom step range below:")

# Mobile-friendly slider bars to set your range anytime
min_steps = st.slider("Minimum Steps", min_value=1000, max_value=20000, value=5000, step=500)
max_steps = st.slider("Maximum Steps", min_value=1000, max_value=30000, value=10000, step=500)

# Make sure min isn't higher than max
if min_steps > max_steps:
    st.error("Error: Minimum steps cannot be higher than Maximum steps!")
else:
    if st.button("Generate Step Goal", key="steps_btn"):
        random_goal = random.randint(min_steps, max_steps)
        # Display the result in a big green callout box
        st.success(f"Today's Goal: {random_goal:,} steps!")

st.write("---")

# ==========================================
# TOOL 2: PC PARTS RANDOMIZER
# ==========================================
st.header("🖥️ PC Build Randomizer")
st.write("Click the button to pick random hardware from your lists.")

# --- CUSTOMIZE YOUR LISTS HERE ---
# You can open your code anytime on GitHub to add more names inside the brackets!
gpus = ["NVIDIA RTX 4090", "NVIDIA RTX 4070", "AMD Radeon 7900 XTX", "Intel Arc A770"]
cpus = ["Intel Core i9-14900K", "AMD Ryzen 7 7800X3D", "Intel Core i5-14600K", "AMD Ryzen 5 7600X"]
ram_options = ["16GB DDR5", "32GB DDR5", "64GB DDR5"]
storage_options = ["1TB NVMe SSD", "2TB NVMe SSD", "4TB NVMe SSD"]
# ---------------------------------

if st.button("Randomize PC Build", key="pc_btn"):
    # Select one random item from each list above
    selected_gpu = random.choice(gpus)
    selected_cpu = random.choice(cpus)
    selected_ram = random.choice(ram_options)
    selected_storage = random.choice(storage_options)
    
    # Display the final generated build neatly
    st.info("📦 Your Generated Build:")
    st.markdown(f"**GPU:** {selected_gpu}")
    st.markdown(f"**CPU:** {selected_cpu}")
    st.markdown(f"**RAM:** {selected_ram}")
    st.markdown(f"**Storage:** {selected_storage}")
