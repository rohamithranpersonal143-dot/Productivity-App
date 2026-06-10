import random
import streamlit as st

# Setup page title and mobile-friendly layout
st.set_page_config(page_title="My Daily Tool", page_icon="🏃‍♂️", layout="centered")

st.title("📱 Stimulation App")
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
gpus = ["NVIDIA GeForce RTX 5090", "NVIDIA GeForce RTX 5080", "NVIDIA GeForce RTX 5070 Ti", "NVIDIA GeForce RTX 5070", "NVIDIA GeForce RTX 5060", "NVIDIA GeForce RTX 4090", "NVIDIA GeForce RTX 4080 Super", "NVIDIA GeForce RTX 4080", "NVIDIA GeForce RTX 4070 Ti Super", "NVIDIA GeForce RTX 4070 Ti", "NVIDIA GeForce RTX 4070 Super", "NVIDIA GeForce RTX 4070", "NVIDIA GeForce RTX 4060 Ti", "NVIDIA GeForce RTX 4060", "NVIDIA GeForce RTX 3090 Ti", "NVIDIA GeForce RTX 3090", "NVIDIA GeForce RTX 3080 Ti", "NVIDIA GeForce RTX 3080", "NVIDIA GeForce RTX 3070 Ti", "NVIDIA GeForce RTX 3070", "NVIDIA GeForce RTX 3060 Ti", "NVIDIA GeForce RTX 3060", "NVIDIA GeForce RTX 3050", "NVIDIA GeForce GTX 1660 Ti", "NVIDIA GeForce GTX 1660 Super", "NVIDIA GeForce GTX 1660", "NVIDIA GeForce GTX 1650 Super", "NVIDIA GeForce GTX 1650", "NVIDIA GeForce GTX 1080 Ti", "NVIDIA GeForce GTX 1080", "NVIDIA GeForce GTX 1070 Ti", "NVIDIA GeForce GTX 1070", "NVIDIA GeForce GTX 1060", "NVIDIA GeForce GTX 1050 Ti", "NVIDIA GeForce GTX 1050", "NVIDIA GeForce GT 1030", "AMD Radeon RX 9070 XT", "AMD Radeon RX 9070 GRE", "AMD Radeon RX 9060 XT", "AMD Radeon RX 7900 XTX", "AMD Radeon RX 7900 XT", "AMD Radeon RX 7900 GRE", "AMD Radeon RX 7800 XT", "AMD Radeon RX 7700 XT", "AMD Radeon RX 7600 XT", "AMD Radeon RX 7600", "AMD Radeon RX 6950 XT", "AMD Radeon RX 6900 XT", "AMD Radeon RX 6800 XT", "AMD Radeon RX 6800", "AMD Radeon RX 6750 XT", "AMD Radeon RX 6700 XT", "AMD Radeon RX 6700", "AMD Radeon RX 6650 XT", "AMD Radeon RX 6600 XT", "AMD Radeon RX 6600", "AMD Radeon RX 6500 XT", "AMD Radeon RX 6400", "AMD Radeon RX 5700 XT", "AMD Radeon RX 5700", "AMD Radeon RX 5600 XT", "AMD Radeon RX 5500 XT", "AMD Radeon RX Vega 64", "AMD Radeon RX Vega 56", "AMD Radeon RX 590", "AMD Radeon RX 580", "AMD Radeon RX 570", "Intel Arc B580", "Intel Arc B570", "Intel Arc A770", "Intel Arc A750", "Intel Arc A580", "Intel Arc A380"]
cpus = ["Intel Core Ultra 9 285K", "Intel Core Ultra 7 270K Plus", "Intel Core Ultra 7 265K", "Intel Core Ultra 5 250K Plus", "Intel Core Ultra 5 245K", "Intel Core i9-14900KS", "Intel Core i9-14900K", "Intel Core i7-14700K", "Intel Core i5-14600K", "Intel Core i9-13900K", "Intel Core i7-13700K", "Intel Core i5-13600K", "Intel Core i9-12900K", "Intel Core i7-12700K", "Intel Core i5-12600K", "Intel Core i7-11700K", "Intel Core i9-10900K", "Intel Core i7-8700K", "Intel Core i7-4790K", "AMD Ryzen 9 9950X3D2", "AMD Ryzen 9 9950X", "AMD Ryzen 9 9900X3D", "AMD Ryzen 9 9900X", "AMD Ryzen 7 9800X3D", "AMD Ryzen 7 9700X", "AMD Ryzen 5 9600X", "AMD Ryzen 9 7950X3D", "AMD Ryzen 9 7950X", "AMD Ryzen 7 7800X3D", "AMD Ryzen 7 7700X3D", "AMD Ryzen 7 7700X", "AMD Ryzen 5 7600X3D", "AMD Ryzen 5 7600X", "AMD Ryzen 7 5800X3D", "AMD Ryzen 7 5700X3D", "AMD Ryzen 9 5950X", "AMD Ryzen 9 5900X", "AMD Ryzen 7 5800X", "AMD Ryzen 5 5600X", "AMD Ryzen 5 5600", "AMD Ryzen 5 3600"]
ram_options = ["8GB DDR4","16GB DDR4", "32GB DDR4", "64GB DDR4", "8GB DDR5" , "16GB DDR5", "32GB DDR5" , "64GB DDR5"]
storage_options = ["128GB NVMe SSD" , "256GB NVMe SSD" , "512GB NVMe SSD", "1TB NVMe SSD", "2TB NVMe SSD", "4TB NVMe SSD"]
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
st.header("💰 Budget-Based PC Builder")
st.write("Type your budget and select your preference to get a working configuration.")

# Input for custom dollar amount
budget = st.number_input(
    "Enter your custom PC budget ($)",
    min_value=0,
    max_value=100000,
    value=1000,
    step=50
)

# Radio selection to determine build strategy
parts_condition = st.radio(
    "What kind of parts are you looking for?",
    options=["Only New Parts", "Include Used Parts"],
    horizontal=True
)

if st.button("Generate Compatible Build", key="budget_btn"):

    # ------------------------------------------
    # STRATEGY A: INCLUDE USED PARTS
    # ------------------------------------------
    if parts_condition == "Include Used Parts":
        if budget < 150:
            st.warning(
                "⚠️ Budgets under $150 are too tight for a custom build. Look for a refurbished office PC on eBay.")

        elif 150 <= budget < 400:
            st.success("📦 **Tier: Ultra-Budget Used King**")
            st.markdown("**CPU:** AMD Ryzen 5 3600 (Used)")
            st.markdown("**Motherboard:** Any budget B450 AM4 Motherboard (Used)")
            st.markdown("**RAM:** 16GB (2x8GB) DDR4 3200MHz")
            st.markdown("**GPU:** AMD Radeon RX 580 8GB or GTX 1660 Super (Used)")
            st.markdown("**Storage:** 512GB NVMe M.2 SSD")
            st.markdown("**Case:** Any budget case under $40")
            st.markdown("**Power Supply:** 500W 80+ Bronze Certified")

        elif 400 <= budget < 800:
            st.success("🚀 **Tier: Mid-Range Value Used Build**")
            st.markdown("**CPU:** AMD Ryzen 5 5600 (Used/New)")
            st.markdown("**Motherboard:** MSI B550M PRO-VDH WiFi")
            st.markdown("**RAM:** 32GB (2x16GB) DDR4 3200MHz")
            st.markdown("**GPU:** NVIDIA RTX 3070 8GB or AMD RX 6700 XT 12GB (Used)")
            st.markdown("**Storage:** 1TB NVMe PCIe 4.0 M.2 SSD")
            st.markdown("**Case:** Montech AIR 100 LITE")
            st.markdown("**Power Supply:** 650W 80+ Gold Certified")

        else:
            st.info(
                "💡 High budgets are better spent on brand-new generation parts. Check out the 'Only New Parts' configuration!")

    # ------------------------------------------
    # STRATEGY B: ONLY NEW PARTS
    # ------------------------------------------
    else:
        if budget < 300:
            st.warning(
                "⚠️ High-performance modern operating parts generally require at least a $300 budget when buying exclusively brand new.")

        elif 300 <= budget < 500:
            st.success("🎮 **Tier: New Ultra-Budget APU Build (No Dedicated GPU)**")
            st.markdown("**CPU:** AMD Ryzen 5 5600G (With AMD Radeon Vega Graphics)")
            st.markdown("**Motherboard:** ASUS Prime B450M-A II")
            st.markdown("**RAM:** 16GB (2x8GB) DDR4 3200MHz")
            st.markdown("**GPU:** Integrated Radeon Graphics (Built into CPU, good for esports/indie games)")
            st.markdown("**Storage:** 512GB NVMe M.2 SSD")
            st.markdown("**Case:** Budget Micro-ATX Case with fans")
            st.markdown("**Power Supply:** 500W 80+ Certified Power Supply")

        elif 500 <= budget < 800:
            st.success("🎮 **Tier: New Entry-Level 1080p Gaming**")
            st.markdown("**CPU:** AMD Ryzen 5 5600 (Includes Cooler)")
            st.markdown("**Motherboard:** MSI B550M PRO-VDH WiFi")
            st.markdown("**RAM:** 16GB (2x8GB) DDR4 3200MHz")
            st.markdown("**GPU:** AMD Radeon RX 6600 8GB")
            st.markdown("**Storage:** 1TB NVMe M.2 SSD")
            st.markdown("**Case:** Montech AIR 100 LITE")
            st.markdown("**Power Supply:** 550W 80+ Bronze Certified")

        elif 800 <= budget < 1500:
            st.success("🔥 **Tier: New Mid-Range 1440p Powerhouse**")
            st.markdown("**CPU:** AMD Ryzen 5 7600X")
            st.markdown("**CPU Cooler:** Thermalright Peerless Assassin 120 SE")
            st.markdown("**Motherboard:** MSI MAG B650 Tomahawk WiFi")
            st.markdown("**RAM:** 32GB (2x16GB) DDR5 6000MHz CL30")
            st.markdown("**GPU:** NVIDIA GeForce RTX 4070 Super 12GB")
            st.markdown("**Storage:** 1TB NVMe PCIe 4.0 M.2 SSD")
            st.markdown("**Case:** Corsair 4000D Airflow ATX")
            st.markdown("**Power Supply:** 750W 80+ Gold Fully Modular")

        else:
            st.success("👑 **Tier: New High-End 4K Ultimate Build**")
            st.markdown("**CPU:** AMD Ryzen 7 7800X3D")
            st.markdown("**CPU Cooler:** Thermalright Phantom Spirit 120 EVO")
            st.markdown("**Motherboard:** Gigabyte X870 AORUS Elite AX")
            st.markdown("**RAM:** 64GB (2x32GB) DDR5 6000MHz CL30")
            st.markdown("**GPU:** NVIDIA GeForce RTX 4080 Super 16GB")
            st.markdown("**Storage:** 2TB NVMe PCIe 4.0 M.2 SSD")
            st.markdown("**Case:** Lian Li Lancool 216 ATX")
            st.markdown("**Power Supply:** 850W 80+ Gold ATX 3.0")
