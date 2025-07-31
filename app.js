/**
 * Chapter Companion - Main Application
 * A spoiler-free character guide for fiction novels
 */

// Application state
const state = {
    seriesData: null,
    currentSeries: null,
    currentBook: null,
    currentChapter: 1,
    bookData: {}  // Cache for loaded book data
};

// Application controller
const app = {
    /**
     * Initialize the application
     */
    async init() {
        try {
            await this.loadSeriesData();
            this.renderSeriesShelf();
        } catch (error) {
            this.showError('Failed to load series data. Please ensure data/series.json exists.');
            console.error('Initialization error:', error);
        }
    },

    /**
     * Load series data from JSON file
     */
    async loadSeriesData() {
        const response = await fetch('data/series.json');
        if (!response.ok) {
            throw new Error(`Failed to load series.json: ${response.status}`);
        }
        state.seriesData = await response.json();
    },

    /**
     * Load book data from JSON file
     */
    async loadBookData(seriesId, bookNumber) {
        const cacheKey = `${seriesId}-${bookNumber}`;
        
        // Return cached data if available
        if (state.bookData[cacheKey]) {
            return state.bookData[cacheKey];
        }

        const response = await fetch(`data/${seriesId}/book${bookNumber}.json`);
        if (!response.ok) {
            throw new Error(`Failed to load book data: ${response.status}`);
        }
        
        const bookData = await response.json();
        state.bookData[cacheKey] = bookData;
        return bookData;
    },

    /**
     * View Management
     */
    showView(viewId) {
        // Hide all views
        document.querySelectorAll('.view').forEach(view => {
            view.classList.remove('active');
        });
        
        // Show selected view
        document.getElementById(viewId).classList.add('active');
    },

    showSeriesView() {
        this.showView('seriesView');
    },

    showBookView() {
        this.showView('bookView');
    },

    showChapterView() {
        this.showView('chapterView');
    },

    /**
     * Series Shelf Rendering
     */
    renderSeriesShelf() {
        const shelf = document.getElementById('seriesShelf');
        shelf.innerHTML = '';

        state.seriesData.series.forEach((series, index) => {
            const book = this.createBookElement(series.title, index, () => {
                this.selectSeries(series);
            });
            shelf.appendChild(book);
        });
    },

    /**
     * Book Shelf Rendering
     */
    renderBookShelf(series) {
        const shelf = document.getElementById('bookShelf');
        shelf.innerHTML = '';

        series.books.forEach((bookTitle, index) => {
            const book = this.createBookElement(bookTitle, index, () => {
                this.selectBook(series.id, index + 1, bookTitle);
            });
            shelf.appendChild(book);
        });
    },

    /**
     * Create a book spine element
     */
    createBookElement(title, index, onClick) {
        const book = document.createElement('div');
        book.className = 'book';
        book.onclick = onClick;

        const spine = document.createElement('div');
        spine.className = `book-spine color-${(index % 8) + 1}`;

        const titleEl = document.createElement('div');
        titleEl.className = 'book-title';
        titleEl.textContent = title;

        spine.appendChild(titleEl);
        book.appendChild(spine);
        return book;
    },

    /**
     * Series Selection
     */
    selectSeries(series) {
        state.currentSeries = series;
        document.getElementById('selectedSeriesTitle').textContent = series.title;
        this.renderBookShelf(series);
        this.showBookView();
    },

    /**
     * Book Selection
     */
    async selectBook(seriesId, bookNumber, bookTitle) {
        try {
            this.showLoading(true);
            
            const bookData = await this.loadBookData(seriesId, bookNumber);
            state.currentBook = {
                seriesId,
                bookNumber,
                title: bookTitle,
                data: bookData
            };

            this.renderChapterView();
            this.showChapterView();
        } catch (error) {
            this.showError(`Failed to load book data. Please ensure data/${seriesId}/book${bookNumber}.json exists.`);
            console.error('Book loading error:', error);
        } finally {
            this.showLoading(false);
        }
    },

    /**
     * Chapter View Rendering
     */
    renderChapterView() {
        const bookData = state.currentBook.data;
        
        // Set book title
        document.getElementById('selectedBookTitle').textContent = state.currentBook.title;
        
        // Populate chapter selector
        const select = document.getElementById('chapterSelect');
        select.innerHTML = '';
        
        bookData.chapters.forEach((chapter, index) => {
            const option = document.createElement('option');
            option.value = index + 1;
            option.textContent = `Chapter ${chapter.number}: ${chapter.title}`;
            select.appendChild(option);
        });
        
        // Reset to chapter 1
        state.currentChapter = 1;
        this.updateChapterDisplay();
    },

    /**
     * Update Chapter Display
     */
    updateChapterDisplay() {
        const chapterIndex = parseInt(document.getElementById('chapterSelect').value) - 1;
        state.currentChapter = chapterIndex + 1;
        
        const chapter = state.currentBook.data.chapters[chapterIndex];
        
        // Update chapter summary
        document.getElementById('chapterSummary').textContent = chapter.summary;
        document.getElementById('chapterSummary').classList.remove('visible');
        
        // Update button text
        const button = document.querySelector('.spoiler-toggle');
        button.textContent = 'Show Chapter Summary';
        
        // Render characters
        this.renderCharacters(chapterIndex);
    },

    /**
     * Render Characters
     */
    renderCharacters(chapterIndex) {
        const chapters = state.currentBook.data.chapters;
        const currentChapter = chapters[chapterIndex];
        
        // Get all characters up to current chapter
        const allCharacters = new Set();
        const currentChapterCharacters = new Set(currentChapter.charactersIntroduced || []);
        
        // Collect all characters introduced up to this chapter
        for (let i = 0; i <= chapterIndex; i++) {
            const ch = chapters[i];
            if (ch.charactersIntroduced) {
                ch.charactersIntroduced.forEach(char => allCharacters.add(char));
            }
        }
        
        // Render current chapter characters
        const currentGrid = document.getElementById('currentChapterCharacters');
        currentGrid.innerHTML = '';
        
        currentChapterCharacters.forEach(charName => {
            if (currentChapter.characters && currentChapter.characters[charName]) {
                const card = this.createCharacterCard(
                    charName, 
                    currentChapter.characters[charName], 
                    true
                );
                currentGrid.appendChild(card);
            }
        });
        
        // Render all other characters
        const allGrid = document.getElementById('allCharacters');
        allGrid.innerHTML = '';
        
        allCharacters.forEach(charName => {
            if (!currentChapterCharacters.has(charName)) {
                // Find the most recent chapter info for this character
                for (let i = chapterIndex; i >= 0; i--) {
                    const ch = chapters[i];
                    if (ch.characters && ch.characters[charName]) {
                        const card = this.createCharacterCard(
                            charName, 
                            ch.characters[charName], 
                            false
                        );
                        allGrid.appendChild(card);
                        break;
                    }
                }
            }
        });
    },

    /**
     * Create Character Card
     */
    createCharacterCard(name, info, isCurrent) {
        const card = document.createElement('div');
        card.className = `character-card ${isCurrent ? 'current-chapter' : ''}`;
        
        const nameEl = document.createElement('div');
        nameEl.className = 'character-name';
        nameEl.textContent = name;
        
        const descEl = document.createElement('div');
        descEl.className = 'character-description';
        descEl.textContent = `${info.background} ${info.arc}`;
        
        card.appendChild(nameEl);
        card.appendChild(descEl);
        return card;
    },

    /**
     * Toggle Spoiler Content
     */
    toggleSpoiler(elementId) {
        const content = document.getElementById(elementId);
        content.classList.toggle('visible');
        
        const button = content.previousElementSibling;
        const isVisible = content.classList.contains('visible');
        button.textContent = isVisible ? 'Hide Chapter Summary' : 'Show Chapter Summary';
    },

    /**
     * UI State Management
     */
    showLoading(show) {
        document.getElementById('loadingState').classList.toggle('hidden', !show);
    },

    showError(message) {
        const errorState = document.getElementById('errorState');
        const errorMessage = errorState.querySelector('.error-message');
        errorMessage.textContent = message;
        errorState.classList.remove('hidden');
        
        // Hide error after 5 seconds
        setTimeout(() => {
            errorState.classList.add('hidden');
        }, 5000);
    }
};

// Initialize app when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    app.init();
});
