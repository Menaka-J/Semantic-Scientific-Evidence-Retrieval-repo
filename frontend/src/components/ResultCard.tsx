interface Props{

    result:any;

}

export default function ResultCard({result}:Props){

    return(

        <div className="bg-white rounded shadow p-5">

            <h2 className="font-bold text-lg">

                {result.title}

            </h2>

            <p className="mt-3">

                {result.abstract}

            </p>

            <div className="mt-3">

                Similarity :

                {result.score.toFixed(4)}

            </div>

        </div>

    );

}