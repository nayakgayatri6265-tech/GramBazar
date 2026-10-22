
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>KalaGram AI | Handmade with Love</title>
<style>
:root {
  --green:#205b43;
  --green2:#347c59;
  --cream:#fffaf0;
  --gold:#e6ad52;
  --ink:#24352b;
  --muted:#6c786f;
}
*{box-sizing:border-box}
body{margin:0;font-family:Arial,sans-serif;background:var(--cream);color:var(--ink)}
button,input,select,textarea{font:inherit}
button{cursor:pointer}
header{position:sticky;top:0;z-index:5;background:#fff;padding:16px 6%;display:flex;justify-content:space-between;align-items:center;gap:16px;box-shadow:0 3px 15px #183b2410}
.logo{font-size:24px;font-weight:900;color:var(--green)}
.logo span{color:var(--gold)}
nav{display:flex;align-items:center;gap:18px;flex-wrap:wrap}
nav a{text-decoration:none;color:var(--ink);font-size:14px;font-weight:bold}
.btn{border:0;background:var(--green);color:white;border-radius:9px;padding:12px 17px;font-weight:bold;transition:.2s}
.btn:hover{background:var(--green2);transform:translateY(-1px)}
.btn.gold{background:var(--gold);color:#2d311e}
.btn.light{background:white;color:var(--green);border:1px solid #cbd9ce}
.hero{padding:70px 7%;display:grid;grid-template-columns:1.15fr .85fr;align-items:center;gap:35px;background:linear-gradient(120deg,#e7f0df,#fff4dd)}
.eyebrow{color:var(--green2);font-size:13px;font-weight:800;letter-spacing:2px;text-transform:uppercase}
.hero h1{font-size:clamp(38px,5vw,65px);line-height:1.06;margin:15px 0}
.hero h1 span{color:var(--green2)}
.hero p{font-size:17px;line-height:1.8;color:#56645a;max-width:550px}
.hero-actions{display:flex;gap:12px;flex-wrap:wrap;margin-top:25px}
.hero-art{min-height:330px;border-radius:28px;background:linear-gradient(145deg,#f5dba8,#e5b66b);display:grid;place-items:center;position:relative;overflow:hidden}
.hero-art .big{font-size:120px;filter:drop-shadow(0 15px 8px #80551e25)}
.floating{position:absolute;background:#fffdf5;padding:12px 16px;border-radius:13px;font-weight:bold;box-shadow:0 8px 25px #59421c1b}
.float1{top:24px;left:20px}.float2{bottom:24px;right:18px}
.benefits{display:grid;grid-template-columns:repeat(3,1fr);gap:15px;padding:25px 7%;background:white}
.benefit{text-align:center;padding:10px}
.benefit strong{display:block;margin:8px}
section{padding:55px 7%}
.section-head{text-align:center;margin-bottom:30px}
.section-head h2{font-size:34px;color:var(--green);margin:0 0 10px}
.section-head p{color:var(--muted);line-height:1.6}
.searchbar{max-width:760px;margin:0 auto 28px;display:flex;gap:10px}
input,select,textarea{width:100%;padding:13px;border:1px solid #d7dfd5;border-radius:9px;background:white;outline:none}
input:focus,select:focus,textarea:focus{border-color:var(--green2);box-shadow:0 0 0 3px #347c5915}
.products{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:20px}
.product{background:white;border:1px solid #eee9dd;border-radius:17px;padding:14px;box-shadow:0 6px 22px #263b2510;transition:.25s}
.product:hover{transform:translateY(-5px);box-shadow:0 12px 30px #263b2517}
.product-art{height:170px;border-radius:12px;background:linear-gradient(140deg,#f6ead1,#e8f0df);display:grid;place-items:center;font-size:70px}
.product h3{margin:15px 0 8px}
.product p{color:var(--muted);font-size:14px;line-height:1.5;min-height:42px}
.price{font-size:22px;font-weight:900;color:var(--green);margin:12px 0}
.product .btn{width:100%}
#no-results{text-align:center;color:var(--muted)}
.cart-section{background:#edf3e9}
.cart-panel{max-width:900px;margin:auto;background:white;border-radius:18px;padding:24px;box-shadow:0 8px 25px #183b2410}
.cart-row{display:flex;justify-content:space-between;align-items:center;gap:12px;padding:12px 0;border-bottom:1px solid #eee}
.cart-row button{border:0;border-radius:6px;background:#f9e7df;padding:8px;color:#a03d27}
.cart-footer{display:flex;align-items:center;justify-content:space-between;gap:15px;flex-wrap:wrap;margin-top:20px}
.cart-total{font-size:24px;font-weight:900;color:var(--green)}
.ai-panel{max-width:650px;margin:auto;padding:25px;background:white;border-radius:18px;box-shadow:0 8px 25px #183b2410}
label{display:block;font-size:14px;font-weight:bold;margin:14px 0 7px}
#ai-result{color:var(--green);line-height:1.7}
footer{background:#173e2e;color:white;padding:35px 7%;text-align:center;line-height:1.8}
footer p{margin:6px}
.modal{display:none;position:fixed;inset:0;z-index:20;background:#10271dcc;padding:18px;overflow-y:auto;align-items:center;justify-content:center}
.modal.show{display:flex}
.modal-card{position:relative;width:100%;max-width:520px;background:white;border-radius:20px;padding:28px;box-shadow:0 20px 70px #0004;margin:auto}
.modal-card h2{color:var(--green);margin:0 35px 8px 0}
.modal-card .sub{color:var(--muted);line-height:1.5;margin-top:0}
.close{position:absolute;right:16px;top:12px;width:36px;height:36px;border:0;border-radius:50%;background:#edf3e9;color:var(--green);font-size:25px}
.form-grid{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.summary{background:#f1f5ec;padding:15px;border-radius:12px;margin:17px 0}
.summary-row{display:flex;justify-content:space-between;gap:12px;margin:8px 0;font-size:14px}
.summary-total{border-top:1px solid #d5dfd2;padding-top:12px;font-weight:900;font-size:19px;color:var(--green)}
.full{width:100%;margin-top:10px}
.status{margin:10px 0;text-align:center;color:var(--green);font-weight:bold}
.small{font-size:12px;color:var(--muted);line-height:1.5}
.link{color:var(--green);font-weight:bold;cursor:pointer;text-decoration:underline}
[hidden]{display:none!important}
@media(max-width:900px){.products{grid-template-columns:repeat(2,minmax(0,1fr))}.hero{grid-template-columns:1fr}.hero-art{min-height:250px}}
@media(max-width:560px){header{justify-content:center}nav{justify-content:center;gap:12px}.hero{padding:45px 6%}.benefits{grid-template-columns:1fr;padding:15px}.products{grid-template-columns:1fr}section{padding:40px 5%}.searchbar{flex-direction:column}.form-grid{grid-template-columns:1fr}.modal-card{padding:22px 17px}.hero-art .big{font-size:95px}}
</style>
</head>
<body>

<header>
  <div class="logo">🌿 KalaGram<span> AI</span></div>
  <nav>
    <a href="#home">Home</a>
    <a href="#products">Shop</a>
    <a href="#ai-finder">Craft Finder</a>
    <a href="#cart">🛒 <span id="cart-count">0</span></a>
    <button class="btn light" id="login-link">Login</button>
    <button class="btn" id="register-link">Join Us</button>
    <span id="user-area" hidden>
      <span id="user-name"></span>
      <button class="btn light" id="logout">Logout</button>
    </span>
  </nav>
</header>

<main>
  <section class="hero" id="home">
    <div>
      <div class="eyebrow">Handcrafted • Heartfelt • Heritage</div>
      <h1>Every Craft Has a <span>Story.</span></h1>
      <p>Bring home the beauty of Indian handmade art. Discover meaningful creations made with traditional skills and a whole lot of love.</p>
      <div class="hero-actions">
        <a href="#products" class="btn">Explore Collection ↗</a>
        <a href="#ai-finder" class="btn light">Find Your Craft</a>
      </div>
    </div>
    <div class="hero-art">
      <span class="floating float1">✨ Made by Artisans</span>
      <span class="big">🧺</span>
      <span class="floating float2">🌿 Rooted in Tradition</span>
    </div>
  </section>

  <div class="benefits">
    <div class="benefit"><span>🧵</span><strong>Handmade Treasures</strong><small>Unique artisan creations</small></div>
    <div class="benefit"><span>🌱</span><strong>Inspired by Nature</strong><small>Traditional materials and art</small></div>
    <div class="benefit"><span>💚</span><strong>Support Local Artisans</strong><small>Celebrate cultural heritage</small></div>
  </div>

  <section id="products">
    <div class="section-head">
      <div class="eyebrow">Our Collection</div>
      <h2>Crafted With Love</h2>
      <p>Find something special for your home, celebrations or someone you love.</p>
    </div>
    <div class="searchbar">
      <input id="search" placeholder="🔍 Search crafts..." aria-label="Search crafts">
      <select id="category" aria-label="Filter category">
        <option value="all">All Categories</option>
        <option value="tribal">Tribal Art</option>
        <option value="seasonal">Seasonal Crafts</option>
        <option value="bamboo">Bamboo Crafts</option>
        <option value="jewellery">Jewellery</option>
      </select>
    </div>
    <div class="products" id="product-list">
      {% for p in products %}
      <article class="product" data-name="{{ p.name|lower }}" data-category="{{ p.category }}" data-price="{{ p.price }}">
        <div class="product-art">{{ p.emoji }}</div>
        <h3>{{ p.name }}</h3>
        <p>{{ p.description }}</p>
        <div class="price">₹{{ p.price }}</div>
        <button class="btn add-cart" data-name="{{ p.name }}" data-price="{{ p.price }}">＋ Add to Cart</button>
      </article>
      {% endfor %}
    </div>
    <p id="no-results" hidden>No matching crafts found. Try another search.</p>
  </section>

  <section id="cart" class="cart-section">
    <div class="section-head">
      <div class="eyebrow">Your Favourites</div>
      <h2>Your Shopping Bag 🛍️</h2>
      <p>Review your selected crafts before placing an order.</p>
    </div>
    <div class="cart-panel">
      <div id="cart-items">Your cart is empty. Explore the collection to add crafts!</div>
      <div class="cart-footer">
        <div class="cart-total" id="cart-total">Total: ₹0</div>
        <div>
          <button class="btn light" id="clear-cart">Clear Cart</button>
          <button class="btn" id="checkout">Order Now →</button>
        </div>
      </div>
    </div>
  </section>

  <section id="ai-finder">
    <div class="section-head">
      <div class="eyebrow">Personalised Picks</div>
      <h2>✨ Craft Finder</h2>
      <p>Tell us your budget and discover crafts that fit.</p>
    </div>
    <div class="ai-panel">
      <label for="budget">Your budget (₹)</label>
      <input type="number" id="budget" min="1" value="500">
      <label for="interest">Choose a category</label>
      <select id="interest">
        <option value="all">Any category</option>
        <option value="tribal">Tribal Art</option>
        <option value="seasonal">Seasonal Crafts</option>
        <option value="bamboo">Bamboo Crafts</option>
        <option value="jewellery">Jewellery</option>
      </select>
      <button class="btn full" id="find-crafts">Find My Crafts ✨</button>
      <p id="ai-result"></p>
      <p class="small">This demo recommends products using your budget and selected category.</p>
    </div>
  </section>
</main>

<footer>
  <h2>🌿 KalaGram AI</h2>
  <p>Keeping traditions alive, one handmade treasure at a time.</p>
  <p>School Project Demo · Made with ❤️ in India</p>
</footer>

<!-- ORDER POPUP -->
<div class="modal" id="order-modal" role="dialog" aria-modal="true" aria-labelledby="order-title">
  <div class="modal-card">
    <button class="close" data-close aria-label="Close">&times;</button>
    <div class="eyebrow">Almost Yours!</div>
    <h2 id="order-title">Complete Your Order 🛍️</h2>
    <p class="sub">Enter your delivery details. Your order summary will be sent to our shop on WhatsApp.</p>
    <div class="summary">
      <div id="order-summary"></div>
      <div class="summary-row summary-total">
        <span>Total</span><span id="order-total">₹0</span>
      </div>
    </div>
    <form id="order-form">
      <div class="form-grid">
        <div>
          <label for="customer-name">Your Name *</label>
          <input id="customer-name" name="customerName" required maxlength="100" autocomplete="name" placeholder="Full name">
        </div>
        <div>
          <label for="customer-phone">Phone Number *</label>
          <input id="customer-phone" name="phone" required type="tel" inputmode="numeric" pattern="[0-9 +()-]{10,18}" maxlength="18" autocomplete="tel" placeholder="Your phone">
        </div>
      </div>
      <label for="customer-address">Delivery Address *</label>
      <textarea id="customer-address" name="address" rows="3" required maxlength="500" autocomplete="street-address" placeholder="House no., street, city, PIN code"></textarea>
      <label for="customer-note">Special Instructions (optional)</label>
      <textarea id="customer-note" name="note" rows="2" maxlength="300" placeholder="Any delivery or product requests?"></textarea>
      <button class="btn full" type="submit">Confirm Order via WhatsApp ↗</button>
      <p class="small">Your WhatsApp app will open with the order message ready. You must press Send to contact the shop. This demo does not process payment.</p>
    </form>
  </div>
</div>

<!-- REGISTER POPUP -->
<div class="modal" id="register-modal" role="dialog" aria-modal="true">
  <div class="modal-card">
    <button class="close" data-close aria-label="Close">&times;</button>
    <h2>Create Your Account</h2>
    <p class="sub">Join the KalaGram community.</p>
    <div class="status" id="register-status" role="status"></div>
    <form id="register-form">
      <label for="reg-name">Full Name</label>
      <input id="reg-name" name="name" required maxlength="100" autocomplete="name">
      <label for="reg-email">Email</label>
      <input id="reg-email" name="email" type="email" required autocomplete="email">
      <label for="reg-password">Password (at least 8 characters)</label>
      <input id="reg-password" name="password" type="password" required minlength="8" autocomplete="new-password">
      <button class="btn full" type="submit">Create Account</button>
    </form>
    <p class="small">Already registered? <a class="link" href="#" id="to-login">Login here</a></p>
  </div>
</div>

<!-- LOGIN POPUP -->
<div class="modal" id="login-modal" role="dialog" aria-modal="true">
  <div class="modal-card">
    <button class="close" data-close aria-label="Close">&times;</button>
    <h2>Welcome Back 👋</h2>
    <p class="sub">Login to your KalaGram account.</p>
    <div class="status" id="login-status" role="status"></div>
    <form id="login-form">
      <label for="login-email">Email</label>
      <input id="login-email" name="email" type="email" required autocomplete="email">
      <label for="login-password">Password</label>
      <input id="login-password" name="password" type="password" required autocomplete="current-password">
      <button class="btn full" type="submit">Login</button>
    </form>
    <p class="small">New here? <a class="link" href="#" id="to-register">Create an account</a></p>
  </div>
</div>

<script>
const cart = [];
const orderModal = document.getElementById("order-modal");
const loginModal = document.getElementById("login-modal");
const registerModal = document.getElementById("register-modal");

// IMPORTANT: Replace with your shop's WhatsApp number.
// India format: 91 + your 10-digit number, digits only.
const WHATSAPP_NUMBER = "916265646757";

function showModal(modal) {
  closeModals();
  modal.classList.add("show");
}
function closeModals() {
  document.querySelectorAll(".modal").forEach(modal => modal.classList.remove("show"));
}
document.querySelectorAll("[data-close]").forEach(button => button.addEventListener("click", closeModals));
document.querySelectorAll(".modal").forEach(modal => modal.addEventListener("click", event => {
  if (event.target === modal) closeModals();
}));
document.addEventListener("keydown", event => {
  if (event.key === "Escape") closeModals();
});

// Account popups
document.getElementById("login-link").onclick = () => showModal(loginModal);
document.getElementById("register-link").onclick = () => showModal(registerModal);
document.getElementById("to-login").onclick = event => {
  event.preventDefault();
  showModal(loginModal);
};
document.getElementById("to-register").onclick = event => {
  event.preventDefault();
  showModal(registerModal);
};

document.getElementById("register-form").onsubmit = async event => {
  event.preventDefault();
  const status = document.getElementById("register-status");
  status.textContent = "Creating account...";
  try {
    const response = await fetch("/register", {method:"POST", body:new FormData(event.target)});
    const data = await response.json();
    if (!response.ok) {
      status.textContent = data.error || "Registration failed.";
      return;
    }
    event.target.reset();
    document.getElementById("login-status").textContent = data.message;
    showModal(loginModal);
  } catch {
    status.textContent = "Could not connect to the server.";
  }
};

document.getElementById("login-form").onsubmit = async event => {
  event.preventDefault();
  const status = document.getElementById("login-status");
  status.textContent = "Logging in...";
  try {
    const response = await fetch("/login", {method:"POST", body:new FormData(event.target)});
    const data = await response.json();
    if (!response.ok) {
      status.textContent = data.error || "Login failed.";
      return;
    }
    event.target.reset();
    closeModals();
    await refreshSession();
    alert(data.message);
  } catch {
    status.textContent = "Could not connect to the server.";
  }
};

async function refreshSession() {
  try {
    const response = await fetch("/me");
    const data = response.ok ? await response.json() : {logged_in:false};
    document.getElementById("user-area").hidden = !data.logged_in;
    document.getElementById("login-link").hidden = data.logged_in;
    document.getElementById("register-link").hidden = data.logged_in;
    document.getElementById("user-name").textContent = data.logged_in ? "Hi, " + data.name : "";
  } catch {}
}

document.getElementById("logout").onclick = async () => {
  const response = await fetch("/logout", {method:"POST"});
  if (response.ok) {
    await refreshSession();
    alert("Logged out successfully.");
  }
};

// Search and filters
function filterProducts() {
  const query = document.getElementById("search").value.toLowerCase().trim();
  const category = document.getElementById("category").value;
  let count = 0;
  document.querySelectorAll(".product").forEach(card => {
    const visible = card.dataset.name.includes(query) &&
      (category === "all" || card.dataset.category === category);
    card.hidden = !visible;
    if (visible) count++;
  });
  document.getElementById("no-results").hidden = count > 0;
}
document.getElementById("search").addEventListener("input", filterProducts);
document.getElementById("category").addEventListener("change", filterProducts);

// Shopping cart
function getTotal() {
  return cart.reduce((total, item) => total + item.price, 0);
}
function updateCart() {
  document.getElementById("cart-count").textContent = cart.length;
  const container = document.getElementById("cart-items");
  container.replaceChildren();

  if (!cart.length) {
    container.textContent = "Your cart is empty. Explore the collection to add crafts!";
  } else {
    cart.forEach((item, index) => {
      const row = document.createElement("div");
      row.className = "cart-row";
      const label = document.createElement("span");
      label.textContent = `${item.name} — ₹${item.price}`;
      const remove = document.createElement("button");
      remove.textContent = "Remove";
      remove.onclick = () => {
        cart.splice(index, 1);
        updateCart();
      };
      row.append(label, remove);
      container.append(row);
    });
  }

  document.getElementById("cart-total").textContent = "Total: ₹" + getTotal();
}
document.querySelectorAll(".add-cart").forEach(button => {
  button.onclick = () => {
    cart.push({name:button.dataset.name, price:Number(button.dataset.price)});
    updateCart();
    button.textContent = "✓ Added!";
    setTimeout(() => button.textContent = "＋ Add to Cart", 900);
  };
});
document.getElementById("clear-cart").onclick = () => {
  cart.length = 0;
  updateCart();
};

// Show order details popup
document.getElementById("checkout").onclick = () => {
  if (!cart.length) {
    alert("Your cart is empty. Please add a craft first.");
    return;
  }

  const summary = document.getElementById("order-summary");
  summary.replaceChildren();

  cart.forEach(item => {
    const row = document.createElement("div");
    row.className = "summary-row";
    const name = document.createElement("span");
    name.textContent = item.name;
    const price = document.createElement("strong");
    price.textContent = "₹" + item.price;
    row.append(name, price);
    summary.append(row);
  });

  document.getElementById("order-total").textContent = "₹" + getTotal();
  showModal(orderModal);
};

// Confirm order and open WhatsApp
document.getElementById("order-form").onsubmit = event => {
  event.preventDefault();

  if (!cart.length) {
    closeModals();
    alert("Your cart is empty.");
    return;
  }

  if (!/^91\d{10}$/.test(WHATSAPP_NUMBER)) {
    alert("Please set your shop WhatsApp number in the code first.");
    return;
  }

  const name = document.getElementById("customer-name").value.trim();
  const phone = document.getElementById("customer-phone").value.trim();
  const address = document.getElementById("customer-address").value.trim();
  const note = document.getElementById("customer-note").value.trim();

  const items = cart.map((item, index) =>
    `${index + 1}. ${item.name} - Rs. ${item.price}`
  ).join("\n");

  const message =
`Hello KalaGram AI! I would like to place an order.

CUSTOMER DETAILS
Name: ${name}
Phone: ${phone}
Delivery Address: ${address}

ORDER ITEMS
${items}

TOTAL: Rs. ${getTotal()}
${note ? "Special Instructions: " + note + "\n" : ""}
Please confirm product availability, delivery charges and delivery details.
Thank you!`;

  const whatsappURL = "https://wa.me/" + WHATSAPP_NUMBER +
    "?text=" + encodeURIComponent(message);

  window.open(whatsappURL, "_blank", "noopener,noreferrer");
};

// Budget-based craft finder
const products = Array.from(document.querySelectorAll(".product")).map(card => ({
  name: card.querySelector("h3").textContent,
  category: card.dataset.category,
  price: Number(card.dataset.price)
}));

document.getElementById("find-crafts").onclick = () => {
  const budget = Number(document.getElementById("budget").value);
  const category = document.getElementById("interest").value;
  const result = document.getElementById("ai-result");

  if (!Number.isFinite(budget) || budget <= 0) {
    result.textContent = "Please enter a valid budget.";
    return;
  }

  const matches = products.filter(product =>
    product.price <= budget &&
    (category === "all" || product.category === category)
  );

  result.textContent = matches.length
    ? "Your suggestions: " + matches.map(p => `${p.name} (₹${p.price})`).join(" • ")
    : "No matches found. Try a higher budget or another category.";
};

refreshSession();
updateCart();
</script>
</body>
</html>
