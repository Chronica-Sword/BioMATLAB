class App {
    constructor() {
        this.currentView = 'home';
        this.currentLevel = null;
        this.currentProblem = null;
        this.container = document.getElementById('app-container');
        
        // Ensure data is loaded
        if (typeof problems === 'undefined') {
            console.error("Data file not loaded.");
        }
        
        this.init();
    }

    init() {
        // Initial render
        this.navigate('home');
    }

    navigate(view) {
        this.currentView = view;
        const template = document.getElementById(`view-${view}`);
        
        if (!template) return;
        
        // Clear container and inject new view
        this.container.innerHTML = '';
        this.container.appendChild(template.content.cloneNode(true));

        // Post-render setup
        if (view === 'levels') {
            // Add entry animations
            document.querySelectorAll('.level-card').forEach((card, index) => {
                card.style.animationDelay = `${index * 0.1}s`;
                card.classList.add('fade-in');
            });
        }
    }

    loadLevel(level) {
        this.currentLevel = level;
        this.navigate('problem');
        
        // Set sidebar title
        const titles = {
            'beginner': 'Başlangıç',
            'intermediate': 'Orta Seviye',
            'advanced': 'Zor Seviye'
        };
        document.getElementById('sidebar-level-title').textContent = titles[level];

        // Populate sidebar
        const levelProblems = problems.filter(p => p.level === level);
        const listContainer = document.getElementById('problem-list');
        listContainer.innerHTML = '';

        levelProblems.forEach((prob, index) => {
            const btn = document.createElement('button');
            btn.className = 'problem-list-item';
            btn.textContent = prob.title;
            btn.onclick = () => this.loadProblem(prob.id);
            listContainer.appendChild(btn);
        });

        // Load first problem by default if exists
        if (levelProblems.length > 0) {
            this.loadProblem(levelProblems[0].id);
        }
    }

    loadProblem(id) {
        this.currentProblem = problems.find(p => p.id === id);
        if (!this.currentProblem) return;

        // Update Active state in sidebar
        document.querySelectorAll('.problem-list-item').forEach(btn => {
            btn.classList.remove('active');
            if(btn.textContent === this.currentProblem.title) {
                btn.classList.add('active');
            }
        });

        // Fill problem content
        document.getElementById('problem-title').textContent = this.currentProblem.title;
        document.getElementById('problem-description').innerHTML = this.currentProblem.description;
        document.getElementById('code-editor').value = this.currentProblem.starter_code;
        
        // Fill solution data but hide panel
        document.getElementById('solution-code').textContent = this.currentProblem.solution_code;
        document.getElementById('solution-output').textContent = this.currentProblem.expected_output;
        document.getElementById('solution-explanation').innerHTML = this.currentProblem.explanation || "<p>Bu problem için detaylı anlatım henüz eklenmemiştir.</p>";
        
        const solPanel = document.getElementById('solution-panel');
        solPanel.classList.add('hidden');
        
        const expPanel = document.getElementById('explanation-panel');
        expPanel.classList.add('hidden');
        
        // Change button texts back
        const btns = document.querySelectorAll('.editor-actions button');
        if(btns.length >= 2) {
            btns[0].textContent = 'Çözümü ve Çıktıyı Göster';
            btns[1].textContent = '📖 Çözümü Anlat';
        }
    }

    toggleSolution() {
        const panel = document.getElementById('solution-panel');
        const expPanel = document.getElementById('explanation-panel');
        const btn = document.querySelectorAll('.editor-actions button')[0];
        
        if (panel.classList.contains('hidden')) {
            panel.classList.remove('hidden');
            expPanel.classList.add('hidden'); // Hide explanation if open
            btn.textContent = 'Çözümü Gizle';
            document.querySelectorAll('.editor-actions button')[1].textContent = '📖 Çözümü Anlat';
            panel.scrollIntoView({ behavior: 'smooth' });
        } else {
            panel.classList.add('hidden');
            btn.textContent = 'Çözümü ve Çıktıyı Göster';
        }
    }

    toggleExplanation() {
        const panel = document.getElementById('explanation-panel');
        const solPanel = document.getElementById('solution-panel');
        const btn = document.querySelectorAll('.editor-actions button')[1];
        
        if (panel.classList.contains('hidden')) {
            panel.classList.remove('hidden');
            solPanel.classList.add('hidden'); // Hide solution if open
            btn.textContent = '📖 Anlatımı Gizle';
            document.querySelectorAll('.editor-actions button')[0].textContent = 'Çözümü ve Çıktıyı Göster';
            panel.scrollIntoView({ behavior: 'smooth' });
        } else {
            panel.classList.add('hidden');
            btn.textContent = '📖 Çözümü Anlat';
        }
    }
}

// Initialize application when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    window.app = new App();
});
