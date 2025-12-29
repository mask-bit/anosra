// API Base URL
const API_URL = "http://localhost:5000/api"

// Helper function to get auth token
function getToken() {
  return localStorage.getItem("token")
}

// Helper function to make API requests
async function apiRequest(endpoint, method = "GET", data = null) {
  const headers = {
    "Content-Type": "application/json",
  }

  const token = getToken()
  if (token) {
    headers["Authorization"] = `Bearer ${token}`
  }

  const config = {
    method,
    headers,
  }

  if (data && method !== "GET") {
    config.body = JSON.stringify(data)
  }

  try {
    const response = await fetch(`${API_URL}${endpoint}`, config)
    const result = await response.json()

    if (!response.ok) {
      throw new Error(result.message || "Erro na requisição")
    }

    return result
  } catch (error) {
    console.error("[v0] API Error:", error)
    throw error
  }
}

// Auth API
const authAPI = {
  login: (email, password) => apiRequest("/auth/login", "POST", { email, password }),
  register: (data) => apiRequest("/auth/register", "POST", data),
  logout: () => {
    localStorage.removeItem("token")
    localStorage.removeItem("user")
    window.location.href = "/login.html"
  },
}

// Business API
const businessAPI = {
  create: (data) => apiRequest("/business", "POST", data),
  getAll: () => apiRequest("/business", "GET"),
  getById: (id) => apiRequest(`/business/${id}`, "GET"),
  update: (id, data) => apiRequest(`/business/${id}`, "PUT", data),
  delete: (id) => apiRequest(`/business/${id}`, "DELETE"),
}

// Expenses API
const expensesAPI = {
  create: (data) => apiRequest("/expenses", "POST", data),
  getAll: (params) => {
    const query = new URLSearchParams(params).toString()
    return apiRequest(`/expenses?${query}`, "GET")
  },
  getById: (id) => apiRequest(`/expenses/${id}`, "GET"),
  update: (id, data) => apiRequest(`/expenses/${id}`, "PUT", data),
  delete: (id) => apiRequest(`/expenses/${id}`, "DELETE"),
  getAnalysis: () => apiRequest("/expenses/analysis", "GET"),
}

// Employees API
const employeesAPI = {
  create: (data) => apiRequest("/employees", "POST", data),
  getAll: () => apiRequest("/employees", "GET"),
  getById: (id) => apiRequest(`/employees/${id}`, "GET"),
  update: (id, data) => apiRequest(`/employees/${id}`, "PUT", data),
  delete: (id) => apiRequest(`/employees/${id}`, "DELETE"),
  getAnalysis: () => apiRequest("/employees/analysis", "GET"),
}

// Reports API
const reportsAPI = {
  getFinancial: (period) => apiRequest(`/reports/financial?period=${period}`, "GET"),
  getEmployees: () => apiRequest("/reports/employees", "GET"),
  getBusiness: () => apiRequest("/reports/business", "GET"),
  getInconsistencies: () => apiRequest("/reports/inconsistencies", "GET"),
  getComparative: (period) => apiRequest(`/reports/comparative?period=${period}`, "GET"),
}

// Integrations API
const integrationsAPI = {
  getStatus: () => apiRequest("/integrations/open-finance/status", "GET"),
  connect: (bankData) => apiRequest("/integrations/open-finance/connect", "POST", bankData),
  disconnect: () => apiRequest("/integrations/open-finance/disconnect", "POST"),
  sync: () => apiRequest("/integrations/open-finance/sync", "POST"),
}

// Settings API
const settingsAPI = {
  get: () => apiRequest("/settings", "GET"),
  update: (data) => apiRequest("/settings", "PUT", data),
  updatePassword: (data) => apiRequest("/settings/password", "PUT", data),
}
