(() => {
  'use strict';
  const root = document.documentElement;
  const themeButton = document.querySelector('.theme-toggle');
  const updateThemeLabel = () => {
    const dark = root.dataset.theme === 'dark';
    themeButton?.setAttribute('aria-label', `Switch to ${dark ? 'light' : 'dark'} theme`);
    themeButton?.setAttribute('aria-pressed', String(dark));
  };
  updateThemeLabel();
  themeButton?.addEventListener('click', () => {
    root.dataset.theme = root.dataset.theme === 'dark' ? 'light' : 'dark';
    try { localStorage.setItem('jiani-theme', root.dataset.theme); } catch (_) {}
    updateThemeLabel();
  });
  const menu = document.querySelector('.primary-nav');
  const menuButton = document.querySelector('.menu-toggle');
  const closeMenu = () => {
    menu?.classList.remove('open');
    menuButton?.setAttribute('aria-expanded', 'false');
    if (menuButton) menuButton.textContent = 'Menu';
  };
  menuButton?.addEventListener('click', () => {
    const open = menu.classList.toggle('open');
    menuButton.setAttribute('aria-expanded', String(open));
    menuButton.textContent = open ? 'Close' : 'Menu';
  });
  menu?.querySelectorAll('a').forEach(link => link.addEventListener('click', closeMenu));
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && menu?.classList.contains('open')) {
      closeMenu();
      menuButton.focus();
    }
  });
  document.querySelectorAll('.filter-button').forEach(button => {
    button.addEventListener('click', () => {
      document.querySelectorAll('.filter-button').forEach(item => item.setAttribute('aria-pressed', String(item === button)));
      let count = 0;
      document.querySelectorAll('.publication').forEach(paper => {
        const visible = button.dataset.filter === 'All' || paper.dataset.category === button.dataset.filter;
        paper.hidden = !visible;
        if (visible) count++;
      });
      document.querySelector('.count').textContent = `${count} ${count === 1 ? 'work' : 'works'}`;
    });
  });
  const dialog = document.querySelector('.citation-dialog');
  const citationData = document.getElementById('citation-data');
  if (dialog && citationData) {
    const citations = JSON.parse(citationData.textContent);
    const pre = dialog.querySelector('pre');
    const status = dialog.querySelector('.copy-status');
    document.querySelectorAll('.cite-button').forEach(button => {
      button.addEventListener('click', () => {
        pre.textContent = citations[button.dataset.cite];
        status.textContent = '';
        dialog.showModal();
      });
    });
    dialog.querySelector('.dialog-close').addEventListener('click', () => dialog.close());
    dialog.querySelector('.copy-citation').addEventListener('click', async () => {
      try {
        await navigator.clipboard.writeText(pre.textContent);
        status.textContent = 'Citation copied to clipboard.';
      } catch (_) {
        const range = document.createRange();
        range.selectNodeContents(pre);
        const selection = window.getSelection();
        selection.removeAllRanges();
        selection.addRange(range);
        status.textContent = 'Citation selected. Press Ctrl+C or ⌘C to copy.';
      }
    });
  }
  document.querySelector('.print-button')?.addEventListener('click', () => window.print());
})();
