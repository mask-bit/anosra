// API Configuration
const API_URL = "http://localhost:5000/api"

// Token Management
const TokenManager = {
  get: () => localStorage.getItem("token"),
  set: (token) => localStorage.setItem("token", token),
  remove: () => localStorage.removeItem("token"),
  exists: () => !!localStorage.getItem("token"),
}

// User Management
const UserManager = {
  get: () => {
    const user = localStorage.getItem("user")
    return user ? JSON.parse(user) : null
  },
  set: (user) => localStorage.setItem("user", JSON.stringify(user)),
  remove: () => localStorage.removeItem("user"),
  exists: () => !!localStorage.getItem("user"),
}

// API Client
class APIClient {
  constructor(baseURL) {
    this.baseURL = baseURL
  }

  async request(endpoint, options = {}) {
    const url = `${this.baseURL}${endpoint}`
    const token = TokenManager.get()

    const config = {
      ...options,
      headers: {
        "Content-Type": "application/json",
        ...options.headers,
      },
    }

    if (token) {
      config.headers["Authorization"] = `Bearer ${token}`
    }

    try {
      const response = await fetch(url, config)
      const data = await response.json()

      if (!response.ok) {
        throw new Error(data.message || "Erro na requisição")
      }

      return data
    } catch (error) {
      console.error("[v0] API Error:", error)
      throw error
    }
  }

  // Auth endpoints
  async login(email, password) {
    const data = await this.request("/auth/login", {
      method: "POST",
      body: JSON.stringify({ email, password }),
    })

    if (data.token) {
      TokenManager.set(data.token)
      UserManager.set(data.user)
    }

    return data
  }

  async register(userData) {
    const data = await this.request("/auth/register", {
      method: "POST",
      body: JSON.stringify(userData),
    })

    if (data.token) {
      TokenManager.set(data.token)
      UserManager.set(data.user)
    }

    return data
  }

  async recoverPassword(email) {
    return this.request("/auth/recover-password", {
      method: "POST",
      body: JSON.stringify({ email }),
    })
  }

  logout() {
    TokenManager.remove()
    UserManager.remove()
    window.location.href = "login.html"
  }

  // Business endpoints
  async createBusiness(businessData) {
    return this.request("/business", {
      method: "POST",
      body: JSON.stringify(businessData),
    })
  }

  async getBusiness() {
    return this.request("/business")
  }

  async updateBusiness(businessData) {
    return this.request("/business", {
      method: "PUT",
      body: JSON.stringify(businessData),
    })
  }

  // Expenses endpoints
  async getExpenses(filters = {}) {
    const params = new URLSearchParams(filters)
    return this.request(`/expenses?${params}`)
  }

  async createExpense(expenseData) {
    return this.request("/expenses", {
      method: "POST",
      body: JSON.stringify(expenseData),
    })
  }

  async updateExpense(id, expenseData) {
    return this.request(`/expenses/${id}`, {
      method: "PUT",
      body: JSON.stringify(expenseData),
    })
  }

  async deleteExpense(id) {
    return this.request(`/expenses/${id}`, {
      method: "DELETE",
    })
  }

  // Employees endpoints
  async getEmployees() {
    return this.request("/employees")
  }

  async createEmployee(employeeData) {
    return this.request("/employees", {
      method: "POST",
      body: JSON.stringify(employeeData),
    })
  }

  async updateEmployee(id, employeeData) {
    return this.request(`/employees/${id}`, {
      method: "PUT",
      body: JSON.stringify(employeeData),
    })
  }

  async deleteEmployee(id) {
    return this.request(`/employees/${id}`, {
      method: "DELETE",
    })
  }

  // Reports endpoints
  async getReports(period = "month") {
    return this.request(`/reports?period=${period}`)
  }

  async getFinancialReport(period) {
    return this.request(`/reports/financial?period=${period}`)
  }

  async getEmployeesReport() {
    return this.request("/reports/employees")
  }

  async getBusinessReport() {
    return this.request("/reports/business")
  }

  async getInconsistenciesReport() {
    return this.request("/reports/inconsistencies")
  }

  async getComparativeReport() {
    return this.request("/reports/comparative")
  }

  // Integration endpoints
  async connectOpenFinance(bankId) {
    return this.request("/integrations/open-finance/connect", {
      method: "POST",
      body: JSON.stringify({ bank_id: bankId }),
    })
  }

  async disconnectOpenFinance() {
    return this.request("/integrations/open-finance/disconnect", {
      method: "POST",
    })
  }

  async syncOpenFinance() {
    return this.request("/integrations/open-finance/sync", {
      method: "POST",
    })
  }

  async getOpenFinanceStatus() {
    return this.request("/integrations/open-finance/status")
  }

  // Settings endpoints
  async getSettings() {
    return this.request("/settings")
  }

  async updateSettings(settings) {
    return this.request("/settings", {
      method: "PUT",
      body: JSON.stringify(settings),
    })
  }

  async changePassword(oldPassword, newPassword) {
    return this.request("/settings/password", {
      method: "PUT",
      body: JSON.stringify({ old_password: oldPassword, new_password: newPassword }),
    })
  }

  async exportData(format = "json") {
    return this.request(`/settings/export?format=${format}`)
  }

  async deleteAccount() {
    return this.request("/settings/account", {
      method: "DELETE",
    })
  }
}

// Global API instance
const api = new APIClient(API_URL)

// Auth Guard - Protect pages that require authentication
function requireAuth() {
  if (!TokenManager.exists()) {
    window.location.href = "login.html"
    return false
  }
  return true
}

// Check if user is already logged in (for login/register pages)
function redirectIfAuthenticated() {
  if (TokenManager.exists()) {
    window.location.href = "dashboard.html"
    return true
  }
  return false
}

// Initialize user info in header
function initializeUserHeader() {
  const user = UserManager.get()
  if (user) {
    const userNameElement = document.getElementById("userName")
    if (userNameElement) {
      userNameElement.textContent = user.store_name || user.owner_name || "Usuário"
    }
  }
}

// Logout handler
function setupLogoutButton() {
  const logoutBtn = document.getElementById("logoutBtn")
  if (logoutBtn) {
    logoutBtn.addEventListener("click", (e) => {
      e.preventDefault()
      if (confirm("Deseja realmente sair?")) {
        api.logout()
      }
    })
  }
}

// Format currency
function formatCurrency(value) {
  return new Intl.NumberFormat("pt-BR", {
    style: "currency",
    currency: "BRL",
  }).format(value)
}

// Format date
function formatDate(dateString) {
  return new Date(dateString).toLocaleDateString("pt-BR")
}

// Show notification
function showNotification(message, type = "success") {
  const notification = document.createElement("div")
  notification.className = `notification notification-${type}`
  notification.textContent = message
  notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background: ${type === "success" ? "#4caf50" : "#f44336"};
        color: white;
        padding: 15px 25px;
        border-radius: 8px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        z-index: 10000;
        animation: slideIn 0.3s ease;
    `

  document.body.appendChild(notification)

  setTimeout(() => {
    notification.style.animation = "slideOut 0.3s ease"
    setTimeout(() => notification.remove(), 300)
  }, 3000)
}

// Add CSS animations
const style = document.createElement("style")
style.textContent = `
    @keyframes slideIn {
        from { transform: translateX(400px); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    @keyframes slideOut {
        from { transform: translateX(0); opacity: 1; }
        to { transform: translateX(400px); opacity: 0; }
    }
`
document.head.appendChild(style)
