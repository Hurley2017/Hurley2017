'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Bootstrap 5 Multiselect with Search, Select All & Clear All</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    .multiselect-container {
      position: relative;
    }

    .dropdown-menu {
      max-height: 300px;
      overflow-y: auto;
      width: 100%;
    }

    .search-box, .action-buttons {
      padding: 8px 12px;
    }

    .search-box input {
      width: 100%;
      padding: 5px;
    }

    .dropdown-item input[type="checkbox"] {
      margin-right: 8px;
    }

    .action-buttons button {
      margin-right: 5px;
    }
  </style>
</head>
<body class="p-5">

<div class="multiselect-container">
  <button class="btn btn-outline-primary w-100 dropdown-toggle" type="button" id="multiselectDropdown" data-bs-toggle="dropdown" aria-expanded="false">
    Select options
  </button>
  <ul class="dropdown-menu" aria-labelledby="multiselectDropdown">
    <li class="search-box">
      <input type="text" id="searchInput" placeholder="Search...">
    </li>
    <li class="action-buttons d-flex justify-content-between">
      <button class="btn btn-sm btn-success" id="selectAllBtn">Select All</button>
      <button class="btn btn-sm btn-danger" id="clearAllBtn">Clear All</button>
    </li>
    <div id="optionsContainer">
      <!-- Options will appear here -->
    </div>
  </ul>
</div>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
<script>
  const options = ['Apple', 'Banana', 'Cherry', 'Date', 'Grape', 'Mango', 'Orange', 'Peach', 'Pear', 'Pineapple', 'Strawberry'];
  const optionsContainer = document.getElementById('optionsContainer');
  const searchInput = document.getElementById('searchInput');
  const dropdownButton = document.getElementById('multiselectDropdown');
  const selectAllBtn = document.getElementById('selectAllBtn');
  const clearAllBtn = document.getElementById('clearAllBtn');

  function renderOptions(filter = '') {
    optionsContainer.innerHTML = '';
    options
      .filter(option => option.toLowerCase().includes(filter.toLowerCase()))
      .forEach(option => {
        const li = document.createElement('li');
        li.className = 'dropdown-item';
        li.innerHTML = `<input type="checkbox" value="${option}"> ${option}`;
        optionsContainer.appendChild(li);
      });
  }

  function updateDropdownText() {
    const selected = [];
    optionsContainer.querySelectorAll('input[type="checkbox"]:checked').forEach(checkbox => {
      selected.push(checkbox.value);
    });
    dropdownButton.innerText = selected.length ? selected.join(', ') : 'Select options';
  }

  searchInput.addEventListener('input', () => {
    renderOptions(searchInput.value);
    updateCheckboxListeners();
  });

  function updateCheckboxListeners() {
    optionsContainer.querySelectorAll('input[type="checkbox"]').forEach(checkbox => {
      checkbox.addEventListener('change', updateDropdownText);
    });
  }

  selectAllBtn.addEventListener('click', () => {
    optionsContainer.querySelectorAll('input[type="checkbox"]').forEach(checkbox => {
      checkbox.checked = true;
    });
    updateDropdownText();
  });

  clearAllBtn.addEventListener('click', () => {
    optionsContainer.querySelectorAll('input[type="checkbox"]').forEach(checkbox => {
      checkbox.checked = false;
    });
    updateDropdownText();
  });

  renderOptions();
  updateCheckboxListeners();
</script>

</body>
</html>'''