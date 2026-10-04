Fayllaringiz ko'rinishiga qarab `.gitignore` tayyorlab olamiz. Keyin esa **`README.md`** faylini yaratamiz.

---

### 1. `.gitignore` fayli

Terminalda `.gitignore` yarating va ichiga vaqtinchalik hamda virtual muhit fayllarini kiriting:

```bash
cat << _EOF_ > .gitignore
venv/
__pycache__/
*.pyc
.vscode/
.idea/
.DS_Store
_EOF_

```

---

### 2. `README.md` fayli

GitHub loyihangizning yuzi bu **`README.md`** faylidir. U loyihangiz nima haqida ekanligini, qanday kutubxonalar ishlatilganini va uni qanday ishga tushirishni ko'rsatib beradi.

Loyihangiz uchun tayyor `README.md` shabloni:

```markdown
# Data Visualization and API Projects 📊

Bu repozitoriy **Python Crash Course** kitobining amaliy loyihalarini o'z ichiga oladi. Loyihada **Matplotlib**, **Plotly Express**, va **Requests** kutubxonalari yordamida ma'lumotlarni vizualizatsiya qilish hamda REST API bilan ishlash o'rganilgan.

## 🚀 Loyiha tarkibi

* **Dice Simulations (`die.py`, `die_visual.py`, `dice_visual.py`):** Oshiqlar (dice) va shashqollarni o'ynatish hamda ehtimolliklar taqsimotini Plotly orqali vizualizatsiya qilish.
* **Random Walk (`random_walk.py`, `rv_visual.py`):** Tasodifiy yurish (Random Walk) simulyatsiyasi va Matplotlib sochma grafigi (scatter plot).
* **Earthquake Data Analysis (`eq_data/`, `eq_world_map.py`):** Dunyo bo'ylab sodir bo'lgan zilzilalar haqidagi JSON ma'lumotlarini o'qish va xaritada aks ettirish.
* **Weather Data (`sitka_highs.py`, `death_valley_highs_lows.py`):** CSV ob-havo ma'lumotlarini (temperatura ko'rsatkichlari) grafikda taqqoslash.
* **GitHub API (`python_repos.py`, `python_repo_visual.py`):** GitHub REST API orqali eng ko'p yulduzcha yig'gan Python loyihalarini interaktiv grafikda ko'rsatish.

## 🛠️ O'rnatish va Ishga tushirish

1. Repozitoriyani klonlang:
   ```bash
   git clone [https://github.com/USER_NOMINGIZ/REPO_NOMINGIZ.git](https://github.com/USER_NOMINGIZ/REPO_NOMINGIZ.git)
   cd REPO_NOMINGIZ

```

2. Virtual muhitni yarating va faollashtiring:
```bash
python3 -m venv venv
source venv/bin/activate

```


3. Kerakli kutubxonalarni o'rnating:
```bash
pip install -r requirements.txt

```


4. Har qanday skriptni ishga tushiring, masalan:
```bash
python3 dice_visual.py

```




