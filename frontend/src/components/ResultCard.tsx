interface Props {
  result: any;
}

export default function ResultCard({ result }: Props) {
  return (
    <div className="bg-white rounded-xl shadow-lg p-6 hover:shadow-xl transition">

      <div className="flex justify-between">

        <h2 className="text-xl font-bold text-slate-800">
          {result.title}
        </h2>

        <div className="bg-blue-600 text-white rounded-lg px-3 py-1 h-fit">
          {result.score.toFixed(3)}
        </div>

      </div>

      <p className="text-gray-700 mt-5 leading-7">
        {result.abstract}
      </p>

      <div className="mt-5 text-gray-500">
        Document ID : {result.doc_id}
      </div>

    </div>
  );
}