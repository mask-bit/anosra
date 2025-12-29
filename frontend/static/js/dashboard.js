// Dashboard functionality
const dashboardData = null

// Declare necessary variables and functions
const checkAuth = () => true // Mock implementation
const getCurrentUser = () => ({ owner_name: "John Doe" }) // Mock implementation
const showLoading = () => console.log("Loading...") // Mock implementation
const hideLoading = () => console.log("Loading hidden") // Mock implementation
const alertSystem = { error: (message) => console.error(message) } // Mock implementation
const formatPercentage = (value) => `${value.toFixed(2)}%` // Mock implementation
const formatCurrency = (value) => `$${value.toFixed(2)}` // Mock implementation
const formatDate = (date) => date.toLocaleDateString() // Mock implementation
const logout = () => console.log("Logged out") // Mock implementation

const businessAPI = {
  getAll: async () => [{ active: true }, { active: false }, { active: true }],
} // Mock implementation

const expensesAPI = {
  getAll: async ({ period }) => [{ amount: "1000.00" }, { amount: "2000.00" }],
} // Mock implementation

const employeesAPI = {
  getAll: async () => [{ name: "Alice" }, { name: "Bob" }, { name: "Charlie" }],
} // Mock implementation

// Initialize dashboard
async function initDashboard() {
  if (!checkAuth()) return

  const user = getCurrentUser()
  if (user) {
    document.getElementById("userName").textContent = user.owner_name || "Usuário"
    document.getElementById("userAvatar").textContent = (user.owner_name || "U")[0].toUpperCase()
  }

  await loadDashboardData()
}

// Load dashboard data
async function loadDashboardData() {
  try {
    showLoading()

    // Load business data
    const businesses = await businessAPI.getAll()
    updateBusinessStats(businesses)

    // Load expenses data
    const expenses = await expensesAPI.getAll({ period: "month" })
    updateExpenseStats(expenses)

    // Load employees data
    const employees = await employeesAPI.getAll()
    updateEmployeeStats(employees)

    // Load recent activity
    await loadRecentActivity()

    hideLoading()
  } catch (error) {
    console.error("[v0] Dashboard load error:", error)
    hideLoading()
    alertSystem.error("Erro ao carregar dados do dashboard")
  }
}

// Update business statistics
function updateBusinessStats(businesses) {
  const activeCount = businesses.filter((b) => b.active).length
  document.getElementById("activeBusinesses").textContent = activeCount

  // Calculate growth (mock data for now)
  const growth = 12.5
  const changeEl = document.getElementById("businessChange")
  changeEl.textContent = formatPercentage(growth)
  changeEl.className = `stat-change ${growth >= 0 ? "positive" : "negative"}`
}

// Update expense statistics
function updateExpenseStats(expenses) {
  const total = expenses.reduce((sum, exp) => sum + Number.parseFloat(exp.amount), 0)
  document.getElementById("monthExpenses").textContent = formatCurrency(total)

  // Calculate change (mock data for now)
  const change = -5.2
  const changeEl = document.getElementById("expenseChange")
  changeEl.textContent = formatPercentage(change)
  changeEl.className = `stat-change ${change >= 0 ? "positive" : "negative"}`
}

// Update employee statistics
function updateEmployeeStats(employees) {
  document.getElementById("employeeCount").textContent = employees.length

  // Calculate profit based on revenue - expenses (mock calculation)
  const revenue = 50000
  const expenses = 35000
  const profit = revenue - expenses

  document.getElementById("currentProfit").textContent = formatCurrency(profit)

  const profitChange = 8.3
  const changeEl = document.getElementById("profitChange")
  changeEl.textContent = formatPercentage(profitChange)
  changeEl.className = `stat-change ${profitChange >= 0 ? "positive" : "negative"}`
}

// Load recent activity
async function loadRecentActivity() {
  const activityEl = document.getElementById("recentActivity")

  // Mock activity data
  const activities = [
    { type: "expense", description: "Nova despesa registrada", date: new Date(), amount: 1500 },
    { type: "business", description: "Negócio atualizado", date: new Date(Date.now() - 86400000) },
    { type: "employee", description: "Funcionário cadastrado", date: new Date(Date.now() - 172800000) },
  ]

  if (activities.length === 0) {
    activityEl.innerHTML = '<p style="color: #999; text-align: center; padding: 40px;">Nenhuma atividade recente</p>'
    return
  }

  activityEl.innerHTML = activities
    .map(
      (activity) => `
        <div style="padding: 12px; border-bottom: 1px solid #e0e0e0;">
            <div style="font-weight: 600;">${activity.description}</div>
            <div style="font-size: 14px; color: #666; margin-top: 4px;">${formatDate(activity.date)}</div>
        </div>
    `,
    )
    .join("")
}

// Toggle sidebar
function toggleSidebar() {
  const sidebar = document.getElementById("sidebar")
  const mainContent = document.getElementById("mainContent")
  sidebar.classList.toggle("collapsed")
  mainContent.classList.toggle("expanded")
}

// Toggle user menu
function toggleUserMenu() {
  // Implement dropdown menu
  const confirmLogout = confirm("Deseja sair?")
  if (confirmLogout) {
    logout()
  }
}

// Update chart based on period
function updateChart() {
  const period = document.getElementById("chartPeriod").value
  console.log("[v0] Updating chart for period:", period)
  // Chart update logic would go here
}

// Initialize on page load
document.addEventListener("DOMContentLoaded", initDashboard)
