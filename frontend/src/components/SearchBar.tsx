import { useState } from "react";

interface Props{

    onSearch:(query:string,method:string)=>void;

}

export default function SearchBar({onSearch}:Props){

    const [query,setQuery]=useState("");

    const [method,setMethod]=useState("tfidf");

    return(

        <div className="flex flex-col gap-4">

            <textarea

            className="border rounded p-3"

            rows={4}

            placeholder="Enter Scientific Claim"

            value={query}

            onChange={(e)=>setQuery(e.target.value)}

            />

            <select

            className="border rounded p-2"

            value={method}

            onChange={(e)=>setMethod(e.target.value)}

            >

                <option value="tfidf">

                    TF-IDF

                </option>

                <option value="bm25">

                    BM25

                </option>

            </select>

            <button

            onClick={()=>onSearch(query,method)}

            className="bg-blue-600 text-white rounded p-3"

            >

                Search

            </button>

        </div>

    );

}