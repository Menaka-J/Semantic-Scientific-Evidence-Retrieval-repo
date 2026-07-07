import { useState } from "react";

interface Props {
  onSearch: (query: string, method: string) => void;
}

export default function SearchBar({ onSearch }: Props) {
  const [query, setQuery] = useState("");
  const [method, setMethod] = useState("tfidf");

  return (
    <div className="bg-white rounded-xl shadow-lg p-8">

      <textarea
        className="w-full border rounded-lg p-4 resize-none"
        rows={5}
        placeholder="Enter a scientific claim..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />

      <div className="flex justify-between items-center mt-6">

        <select
          value={method}
          onChange={(e) => setMethod(e.target.value)}
          className="border rounded-lg p-3"
        >
          <option value="tfidf">TF-IDF</option>
          <option value="bm25">BM25</option>
        </select>

        <button
          onClick={() => onSearch(query, method)}
          className="bg-blue-700 text-white px-8 py-3 rounded-lg hover:bg-blue-800 transition"
        >
          Search
        </button>

      </div>

    </div>
  );
}