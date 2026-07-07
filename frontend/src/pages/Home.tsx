import { useState } from "react";
import api from "../services/api";
import SearchBar from "../components/SearchBar";
import ResultCard from "../components/ResultCard";

interface SearchResult {
  doc_id: number;
  title: string;
  abstract: string;
  score: number;
  raw_score?: number;
}

export default function Home() {
  const [results, setResults] = useState<SearchResult[]>([]);
  const [loading, setLoading] = useState(false);
  const [method, setMethod] = useState("");

  const search = async (query: string, retrievalMethod: string) => {
    if (!query.trim()) {
      alert("Please enter a scientific claim.");
      return;
    }

    setLoading(true);
    setMethod(retrievalMethod);

    try {
      const response = await api.get(`/search/${retrievalMethod}`, {
        params: {
          query,
          top_k: 10,
        },
      });

      setResults(response.data.results);
    } catch (error) {
      console.error(error);
      alert("Search failed.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-slate-100">

      <div className="max-w-6xl mx-auto p-10">

        <h1 className="text-5xl font-bold text-center text-blue-700">
          Semantic Scientific Evidence Retrieval
        </h1>

        <p className="text-center text-gray-600 mt-3">
          Search scientific evidence using Traditional Information Retrieval.
        </p>

        <div className="mt-10">
          <SearchBar onSearch={search} />
        </div>

        {loading && (
          <div className="text-center mt-8 text-xl font-semibold">
            Searching...
          </div>
        )}

        {!loading && results.length > 0 && (
          <>
            <h2 className="text-2xl font-bold mt-10 mb-6">
              Results using {method.toUpperCase()}
            </h2>

            <div className="space-y-6">
              {results.map((paper) => (
                <ResultCard
                  key={paper.doc_id}
                  result={paper}
                />
              ))}
            </div>
          </>
        )}

      </div>

    </div>
  );
}