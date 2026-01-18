<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Burhani Electricals | Professional Repair Services</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        .hero-gradient { background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%); }
        .category-card { cursor: pointer; transition: all 0.3s ease; border: 2px solid transparent; }
        .category-card:hover { border-color: #3b82f6; transform: translateY(-5px); }
        .modal { display: none; position: fixed; inset: 0; background: rgba(0,0,0,0.7); z-index: 50; align-items: center; justify-content: center; padding: 20px; }
        .modal.active { display: flex; }
    </style>
</head>
<body class="bg-gray-50 font-sans">

    <header class="hero-gradient text-white py-12 px-6 text-center">
        <h1 class="text-4xl font-bold mb-2">Burhani Electricals</h1>
        <p class="text-lg opacity-90">Expert Service & Repairing Since Years</p>
        <div class="mt-6">
            <a href="https://wa.me/918780514062" class="bg-green-500 hover:bg-green-600 text-white font-bold py-3 px-8 rounded-full inline-flex items-center shadow-lg">
                <i class="fab fa-whatsapp mr-2 text-xl"></i> Chat on WhatsApp
            </a>
        </div>
    </header>

    <section class="max-w-6xl mx-auto py-12 px-6">
        <h2 class="text-2xl font-bold text-center text-gray-800 mb-8">What do you need repaired?</h2>
        <p class="text-center text-gray-500 mb-10 -mt-6">Click on any item to see details</p>
        
        <div class="grid grid-cols-2 md:grid-cols-5 gap-4">
            <div onclick="openModal('Fans', 'We specialize in repairing and coil winding for all types of Fans: Ceiling Fans, Table Fans, Exhaust Fans, Wall Fans, and Pedestal Fans.')" class="category-card bg-white p-6 rounded-xl shadow-sm text-center">
                <i class="fas fa-fan text-blue-600 text-3xl mb-3"></i>
                <h3 class="font-bold">Fans</h3>
            </div>

            <div onclick="openModal('Juice Machine', 'Professional repair for all Juice Machines and Extractors. We fix motor issues, blade replacements, and electrical faults.')" class="category-card bg-white p-6 rounded-xl shadow-sm text-center">
                <i class="fas fa-blender text-purple-600 text-3xl mb-3"></i>
                <h3 class="font-bold">Juice Machine</h3>
            </div>

            <div onclick="openModal('Blenders & Grinders', 'We repair all types of Blenders, Grinders, and Mixer-Grinders. Services include coupler replacement, motor repair, and carbon changes.')" class="category-card bg-white p-6 rounded-xl shadow-sm text-center">
                <i class="fas fa-utensils text-pink-600 text-3xl mb-3"></i>
                <h3 class="font-bold">Blender</h3>
            </div>

            <div onclick="openModal('Pressure Cookers', 'Complete servicing for all brands of Pressure Cookers. We replace gaskets, safety valves, whistles, and handles.')" class="category-card bg-white p-6 rounded-xl shadow-sm text-center">
                <i class="fas fa-cloud text-gray-600 text-3xl mb-3"></i>
                <h3 class="font-bold">Cooker</h3>
            </div>

            <div onclick="openModal('Gas Stoves', 'Safe and reliable repair for Single, Double, and Multi-burner Gas Stoves. We fix gas leakage, burner cleaning, and knob replacements.')" class="category-card bg-white p-6 rounded-xl shadow-sm text-center">
                <i class="fas fa-fire text-orange-600 text-3xl mb-3"></i>
                <h3 class="font-bold">Gas Stove</h3>
            </div>
        </div>
    </section>

    <div id="repairModal" class="modal">
        <div class="bg-white rounded-2xl p-8 max-w-md w-full relative">
            <button onclick="closeModal()" class="absolute top-4 right-4 text-gray-400 hover:text-gray-600">
                <i class="fas fa-times text-xl"></i>
            </button>
            <h2 id="modalTitle" class="text-2xl font-bold text-blue-600 mb-4"></h2>
            <p id="modalDescription" class="text-gray-600 mb-6 leading-relaxed"></p>
            <a href="https://wa.me/918780514062" class="block text-center bg-blue-600 text-white font-bold py-3 rounded-lg">
                Enquire for Repair
            </a>
        </div>
    </div>

    <section class="bg-gray-100 py-12 px-6">
        <div class="max-w-4xl mx-auto text-center">
            <h2 class="text-2xl font-bold mb-6 text-gray-800">Contact Details</h2>
            <div class="bg-white p-8 rounded-2xl shadow-sm inline-block text-left w-full md:w-auto">
                <p class="mb-2"><strong><i class="fas fa-user mr-2 text-blue-600"></i> Name:</strong> Husain Vankanerwala</p>
                <p class="mb-2"><strong><i class="fas fa-phone mr-2 text-blue-600"></i> Phone:</strong> +91 8780514062</p>
                <p class="mb-0"><strong><i class="fas fa-envelope mr-2 text-blue-600"></i> Email:</strong> vankanerwalahusain@gmail.com</p>
            </div>
        </div>
    </section>

    <footer class="py-6 text-center text-gray-400 text-xs">
        &copy; 2024 Burhani Electricals | Designed for Reference
    </footer>

    <script>
        function openModal(title, desc) {
            document.getElementById('modalTitle').innerText = title;
            document.getElementById('modalDescription').innerText = desc;
            document.getElementById('repairModal').classList.add('active');
        }
        function closeModal() {
            document.getElementById('repairModal').classList.remove('active');
        }
        // Close modal when clicking outside the box
        window.onclick = function(event) {
            let modal = document.getElementById('repairModal');
            if (event.target == modal) {
                closeModal();
            }
        }
    </script>
</body>
</html>
