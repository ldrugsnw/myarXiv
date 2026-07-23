export interface Paper {
    id: string;
    title: string;
    authors: string[];
    published: string;
    updated: string;
    summary: string;
    pdf_url: string;
}

// python 에서는 published랑 updated를 datetime으로 보냇지만
// React에서는 string이 맞다. 