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

// Check if user is authenticated
function isAuthenticated() {
  const token = localStorage.getItem("token")
  return !!token
}

// Get current user data
function getCurrentUser() {
  const userStr = localStorage.getItem("user")
  try {
    return userStr ? JSON.parse(userStr) : null
  } catch (error) {
    console.error("[v0] Error parsing user data:", error)
    return null
  }
}

// Require authentication - redirect to login if not authenticated
function requireAuth() {
  if (!isAuthenticated()) {
    window.location.href = "/login"
    return false
  }
  return true
}

// Redirect if already authenticated
function redirectIfAuthenticated() {
  if (isAuthenticated()) {
    window.location.href = "/dashboard"
    return true
  }
  return false
}

// Main API object
const api = {
  // Auth methods
  login: async (email, password) => {
    const result = await apiRequest("/auth/login", "POST", { email, password })
    if (result.token) {
      localStorage.setItem("token", result.token)
      if (result.user) {
        localStorage.setItem("user", JSON.stringify(result.user))
      }
    }
    return result
  },

  register: async (data) => {
    const result = await apiRequest("/auth/register", "POST", data)
    if (result.token) {
      localStorage.setItem("token", result.token)
      if (result.user) {
        localStorage.setItem("user", JSON.stringify(result.user))
      }
    }
    return result
  },

  logout: () => {
    localStorage.removeItem("token")
    localStorage.removeItem("user")
    window.location.href = "/login"
  },

  // Helper methods
  isAuthenticated,
  getCurrentUser,
  requireAuth,
  redirectIfAuthenticated,

  // Business methods
  business: {
    create: (data) => apiRequest("/business", "POST", data),
    getAll: () => apiRequest("/business", "GET"),
    getById: (id) => apiRequest(`/business/${id}`, "GET"),
    update: (id, data) => apiRequest(`/business/${id}`, "PUT", data),
    delete: (id) => apiRequest(`/business/${id}`, "DELETE"),
  },

  // Expenses methods
  expenses: {
    create: (data) => apiRequest("/expenses", "POST", data),
    getAll: (params) => {
      const query = new URLSearchParams(params).toString()
      return apiRequest(`/expenses?${query}`, "GET")
    },
    getById: (id) => apiRequest(`/expenses/${id}`, "GET"),
    update: (id, data) => apiRequest(`/expenses/${id}`, "PUT", data),
    delete: (id) => apiRequest(`/expenses/${id}`, "DELETE"),
    getAnalysis: () => apiRequest("/expenses/analysis", "GET"),
  },

  // Employees methods
  employees: {
    create: (data) => apiRequest("/employees", "POST", data),
    getAll: () => apiRequest("/employees", "GET"),
    getById: (id) => apiRequest(`/employees/${id}`, "GET"),
    update: (id, data) => apiRequest(`/employees/${id}`, "PUT", data),
    delete: (id) => apiRequest(`/employees/${id}`, "DELETE"),
    getAnalysis: () => apiRequest("/employees/analysis", "GET"),
  },

  // Reports methods
  reports: {
    getFinancial: (period) => apiRequest(`/reports/financial?period=${period}`, "GET"),
    getEmployees: () => apiRequest("/reports/employees", "GET"),
    getBusiness: () => apiRequest("/reports/business", "GET"),
    getInconsistencies: () => apiRequest("/reports/inconsistencies", "GET"),
    getComparative: (period) => apiRequest(`/reports/comparative?period=${period}`, "GET"),
  },

  // Integrations methods
  integrations: {
    getStatus: () => apiRequest("/integrations/open-finance/status", "GET"),
    connect: (bankData) => apiRequest("/integrations/open-finance/connect", "POST", bankData),
    disconnect: () => apiRequest("/integrations/open-finance/disconnect", "POST"),
    sync: () => apiRequest("/integrations/open-finance/sync", "POST"),
  },

  // Settings methods
  settings: {
    get: () => apiRequest("/settings", "GET"),
    update: (data) => apiRequest("/settings", "PUT", data),
    updatePassword: (data) => apiRequest("/settings/password", "PUT", data),
  },
}

// Legacy compatibility
const authAPI = api
const businessAPI = api.business
const expensesAPI = api.expenses
const employeesAPI = api.employees
const reportsAPI = api.reports
const integrationsAPI = api.integrations
const settingsAPI = api.settings
