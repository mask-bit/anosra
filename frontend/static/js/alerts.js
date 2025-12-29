// Alert System
class AlertSystem {
  constructor() {
    this.alerts = []
    this.container = null
    this.init()
  }

  init() {
    // Create alerts container
    this.container = document.createElement("div")
    this.container.id = "alerts-container"
    this.container.style.cssText = `
            position: fixed;
            top: 80px;
            right: 24px;
            z-index: 9999;
            max-width: 400px;
        `
    document.body.appendChild(this.container)
  }

  show(message, type = "info", duration = 5000) {
    const alert = document.createElement("div")
    alert.className = `alert alert-${type}`
    alert.style.cssText = `
            margin-bottom: 12px;
            animation: slideIn 0.3s ease;
        `

    const icon = this.getIcon(type)
    alert.innerHTML = `
            <span style="font-size: 20px; margin-right: 12px;">${icon}</span>
            <span>${message}</span>
            <button onclick="this.parentElement.remove()" style="margin-left: auto; background: none; border: none; cursor: pointer; font-size: 20px;">×</button>
        `

    this.container.appendChild(alert)

    if (duration > 0) {
      setTimeout(() => {
        alert.style.animation = "slideOut 0.3s ease"
        setTimeout(() => alert.remove(), 300)
      }, duration)
    }
  }

  getIcon(type) {
    const icons = {
      success: "✓",
      error: "✕",
      warning: "⚠",
      info: "ℹ",
    }
    return icons[type] || icons.info
  }

  success(message, duration) {
    this.show(message, "success", duration)
  }

  error(message, duration) {
    this.show(message, "error", duration)
  }

  warning(message, duration) {
    this.show(message, "warning", duration)
  }

  info(message, duration) {
    this.show(message, "info", duration)
  }
}

// Create global alert system instance
const alertSystem = new AlertSystem()

// Add CSS animations
const style = document.createElement("style")
style.textContent = `
    @keyframes slideIn {
        from {
            transform: translateX(400px);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
    
    @keyframes slideOut {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(400px);
            opacity: 0;
        }
    }
`
document.head.appendChild(style)
