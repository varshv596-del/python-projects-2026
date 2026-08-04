const form = document.getElementById("transactionForm");
const text = document.getElementById("text");
const amount = document.getElementById("amount");
const category = document.getElementById("category");
const list = document.getElementById("transactionList");
const balance = document.getElementById("balance");
const income = document.getElementById("income");
const expense = document.getElementById("expense");
const search = document.getElementById("search");
const themeBtn = document.getElementById("themeBtn");

let transactions = JSON.parse(localStorage.getItem("transactions")) || [];
let chart;

form.addEventListener("submit", (e) => {
    e.preventDefault();

    const transaction = {
        id: Date.now(),
        text: text.value,
        amount: Number(amount.value),
        category: category.value
    };

    transactions.push(transaction);

    saveData();

    form.reset();
});

function saveData() {
    localStorage.setItem("transactions", JSON.stringify(transactions));
    updateUI();
}

function updateUI() {

    list.innerHTML = "";

    let incomeTotal = 0;
    let expenseTotal = 0;

    transactions.forEach((t) => {

        const li = document.createElement("li");

        li.innerHTML = `
        <div>
            <strong>${t.text}</strong><br>
            <small>${t.category}</small>
        </div>

        <div>
            ₹${t.amount}
            <button class="delete-btn" onclick="deleteTransaction(${t.id})">
                X
            </button>
        </div>
        `;

        list.appendChild(li);

        if (t.amount > 0)
            incomeTotal += t.amount;
        else
            expenseTotal += t.amount;

    });

    income.textContent = "₹" + incomeTotal;
expense.textContent = "₹" + Math.abs(expenseTotal);
balance.textContent = "₹" + (incomeTotal + expenseTotal);

updateChart(incomeTotal, expenseTotal);

}

function deleteTransaction(id) {

    transactions = transactions.filter((t) => t.id !== id);

    saveData();

}

search.addEventListener("keyup", () => {

    const value = search.value.toLowerCase();

    document.querySelectorAll("#transactionList li").forEach((item) => {

        item.style.display =
            item.innerText.toLowerCase().includes(value)
                ? "flex"
                : "none";

    });

});

function updateChart(incomeTotal, expenseTotal) {

    const ctx = document.getElementById("expenseChart").getContext("2d");

    if (chart) {
        chart.destroy();
    }

    chart = new Chart(ctx, {

        type: "doughnut",

        data: {

            labels: ["Income", "Expense"],

            datasets: [{
                data: [incomeTotal, Math.abs(expenseTotal)],
                backgroundColor: [
                    "#22c55e",
                    "#ef4444"
                ]
            }]

        },

        options: {

            responsive: true,

            plugins: {

                legend: {
                    position: "bottom"
                }

            }

        }

    });

}themeBtn.addEventListener("click", () => {

    document.body.classList.toggle("dark");

    if (document.body.classList.contains("dark")) {
        themeBtn.textContent = "☀️ Light Mode";
    } else {
        themeBtn.textContent = "🌙 Dark Mode";
    }

});

updateUI();