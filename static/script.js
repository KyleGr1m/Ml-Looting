function copyToClipboard(text) {
  navigator.clipboard.writeText(text).then(() => {
    alert('Copied!');
  });
}

function showInfo(button, fullInfo) {
  const row = button.closest('tr');
  let infoRow = document.createElement('tr');
  infoRow.innerHTML = `<td colspan="4">${fullInfo}</td>`;
  row.parentNode.insertBefore(infoRow, row.nextSibling);
  button.disabled = true;
}

function markChecked(checkbox) {
  if (checkbox.checked) {
    checkbox.closest('tr').style.backgroundColor = '#d3ffd3';
  } else {
    checkbox.closest('tr').style.backgroundColor = '';
  }
}
