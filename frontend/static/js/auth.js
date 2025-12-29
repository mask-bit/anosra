// Declare authAPI variable before using it
const authAPI = {
  login: async (email, password) => {
    // Placeholder for actual login logic
    return { token: "fakeToken", user: { first_login: true } }
  },
  register: async (userData) => {
    // Placeholder for actual register logic
    return { token: "fakeToken", user: { first_login: true } }
  },
  logout: () => {
    // Placeholder for actual logout logic
    localStorage.removeItem("token")
    localStorage.removeItem("user")
  },
}

// Login function
async function login(email, password) {
  try {
    const response = await authAPI.login(email, password)

    if (response.token) {
      localStorage.setItem("token", response.token)
      localStorage.setItem("user", JSON.stringify(response.user))

      showAlert("Login realizado com sucesso!", "success")

      // Redirect based on user status
      setTimeout(() => {
        if (response.user.first_login) {
          window.location.href = "/negocios.html"
        } else {
          window.location.href = "/dashboard.html"
        }
      }, 1000)
    }
  } catch (error) {
    showAlert(error.message || "Erro ao fazer login", "error")
  }
}

// Register function
async function register(storeName, ownerName, email, password) {
  try {
    const response = await authAPI.register({
      store_name: storeName,
      owner_name: ownerName,
      email: email,
      password: password,
    })

    if (response.token) {
      localStorage.setItem("token", response.token)
      localStorage.setItem("user", JSON.stringify(response.user))

      showAlert("Conta criada com sucesso!", "success")

      // Redirect to onboarding
      setTimeout(() => {
        window.location.href = "/negocios.html"
      }, 1000)
    }
  } catch (error) {
    showAlert(error.message || "Erro ao criar conta", "error")
  }
}

// Check if user is authenticated
function checkAuth() {
  const token = localStorage.getItem("token")
  if (!token) {
    window.location.href = "/login.html"
    return false
  }
  return true
}

// Get current user
function getCurrentUser() {
  const userStr = localStorage.getItem("user")
  return userStr ? JSON.parse(userStr) : null
}

// Logout function
function logout() {
  authAPI.logout()
}

// Show alert message
function showAlert(message, type = "info") {
  const alertDiv = document.createElement("div")
  alertDiv.className = `alert alert-${type}`
  alertDiv.textContent = message

  document.body.insertBefore(alertDiv, document.body.firstChild)

  setTimeout(() => {
    alertDiv.remove()
  }, 5000)
}
