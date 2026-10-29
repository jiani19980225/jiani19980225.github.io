(() => {
  'use strict';
  const root = document.documentElement;

  const copyText = async (text, source, status, done) => {
    try {
      await navigator.clipboard.writeText(text);
      status.textContent = done;
    } catch (_) {
      const range = document.createRange();
      range.selectNodeContents(source);
      const selection = window.getSelection();
      selection.removeAllRanges();
      selection.addRange(range);
      status.textContent = 'Text selected. Press Ctrl+C or ⌘C to copy.';
    }
  };

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
  const setMenu = open => {
    menu?.classList.toggle('open', open);
    menuButton?.setAttribute('aria-expanded', String(open));
    menuButton?.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
  };
  menuButton?.addEventListener('click', () => setMenu(!menu.classList.contains('open')));
  menu?.querySelectorAll('a').forEach(link => link.addEventListener('click', () => setMenu(false)));
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && menu?.classList.contains('open')) {
      setMenu(false);
      menuButton.focus();
    }
  });

  const filterButtons = document.querySelectorAll('.filter-button');
  filterButtons.forEach(button => {
    button.addEventListener('click', () => {
      const filter = button.dataset.filter;
      filterButtons.forEach(item => item.setAttribute('aria-pressed', String(item === button)));
      let count = 0;
      document.querySelectorAll('.pub').forEach(paper => {
        paper.hidden = filter !== 'all' && paper.dataset.stream !== filter;
        if (!paper.hidden) count++;
      });
      document.querySelectorAll('.pub-group').forEach(group => {
        group.hidden = !group.querySelector('.pub:not([hidden])');
      });
      document.querySelector('.count').textContent = `${count} ${count === 1 ? 'paper' : 'papers'}`;
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
    dialog.addEventListener('click', event => {
      const box = dialog.getBoundingClientRect();
      const outside = event.clientX < box.left || event.clientX > box.right || event.clientY < box.top || event.clientY > box.bottom;
      if (event.target === dialog && outside) dialog.close();
    });
    dialog.querySelector('.copy-citation').addEventListener('click', () => copyText(pre.textContent, pre, status, 'Citation copied to clipboard.'));
  }

  document.querySelectorAll('.copy-bio').forEach(button => {
    const source = document.querySelector(button.dataset.copy);
    const status = button.parentElement.querySelector('.copy-status');
    button.addEventListener('click', () => copyText(source.textContent, source, status, 'Bio copied to clipboard.'));
  });

  document.querySelector('.print-button')?.addEventListener('click', () => window.print());
})();
