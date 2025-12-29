// Format currency
function formatCurrency(value) {
  return new Intl.NumberFormat("pt-BR", {
    style: "currency",
    currency: "BRL",
  }).format(value)
}

// Format date
function formatDate(dateString) {
  const date = new Date(dateString)
  return new Intl.DateTimeFormat("pt-BR").format(date)
}

// Format percentage
function formatPercentage(value) {
  return `${value > 0 ? "+" : ""}${value.toFixed(1)}%`
}

// Validate email
function validateEmail(email) {
  const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
  return re.test(email)
}

// Validate password strength
function validatePassword(password) {
  return password.length >= 8
}

// Debounce function
function debounce(func, wait) {
  let timeout
  return function executedFunction(...args) {
    const later = () => {
      clearTimeout(timeout)
      func(...args)
    }
    clearTimeout(timeout)
    timeout = setTimeout(later, wait)
  }
}

// Show loading spinner
function showLoading() {
  const loader = document.createElement("div")
  loader.id = "loading-spinner"
  loader.innerHTML = '<div class="spinner"></div>'
  document.body.appendChild(loader)
}

// Hide loading spinner
function hideLoading() {
  const loader = document.getElementById("loading-spinner")
  if (loader) {
    loader.remove()
  }
}

// Copy to clipboard
async function copyToClipboard(text) {
  try {
    await navigator.clipboard.writeText(text)
    showAlert("Copiado para área de transferência!", "success")
  } catch (error) {
    showAlert("Erro ao copiar", "error")
  }
}

// Download file
function downloadFile(data, filename, type) {
  const blob = new Blob([data], { type })
  const url = window.URL.createObjectURL(blob)
  const a = document.createElement("a")
  a.href = url
  a.download = filename
  document.body.appendChild(a)
  a.click()
  document.body.removeChild(a)
  window.URL.revokeObjectURL(url)
}

// Show alert function (assuming it needs to be declared)
function showAlert(message, type) {
  const alert = document.createElement("div")
  alert.className = `alert ${type}`
  alert.textContent = message
  document.body.appendChild(alert)
  setTimeout(() => {
    alert.remove()
  }, 3000)
}
