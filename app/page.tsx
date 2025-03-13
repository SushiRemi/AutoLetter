import Image from "next/image";

export default function Home() {
  return (
    <div className="grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]">
      <main className="flex flex-col gap-8 row-start-2 items-center sm:items-start">
        <div className="text-4xl font-bold"> Welcome to AutoLetter! (A LinkedIn API agent)</div>
        <div className="flex flex-row items-center gap-10 max-w-200"> 
          <Image
            src="/lia.pi-logo.jpg"
            alt="LIA.pi logo"
            width={500}
            height={38}
            priority
          />
          <p className="description">
            AutoLetter is an AI Agent that assists in the job application process by creating cover letters for you! 
            By logging into your LinkedIn account, the agent can read your resume/job experience portfolio and
            recommend jobs for you to easily create personalized cover letters.
          </p>
        </div>

        <h2 className="text-2xl">
          How to use AutoLetter:
        </h2>
        <ol className="list-inside list-decimal text-sm text-center sm:text-left font-[family-name:var(--font-geist-mono)]">
          <li>Login to your LinkedIn Account</li>
          <li>Choose from a list of recommended jobs</li>
          <li>Review and download the generated cover letter(s)!</li>
        </ol>

        <div className="flex gap-4 items-center flex-col sm:flex-row">
          <a
            className="rounded-full border border-solid border-black/[.9] dark:border-white/[.9] transition-colors flex items-center justify-center bg-foreground text-background gap-2 hover:bg-[#383838] dark:hover:bg-[#ccc] text-sm sm:text-base h-10 sm:h-12 px-4 sm:px-5"
            href="https://vercel.com/new?utm_source=create-next-app&utm_medium=appdir-template-tw&utm_campaign=create-next-app"
            target="_blank"
            rel="noopener noreferrer"
          >
            <Image
              className="invert-100 dark:invert-0"
              src="/vercel.svg"
              alt="Vercel logomark"
              width={20}
              height={20}
            />
            Start
          </a>

          <a
            className="rounded-full border border-solid border-black/[.3] dark:border-white/[.3] transition-colors flex items-center justify-center hover:bg-[#f2f2f2] dark:hover:bg-[#1a1a1a] hover:border-transparent text-sm sm:text-base h-10 sm:h-12 px-4 sm:px-5 sm:min-w-44"
            href="https://nextjs.org/docs?utm_source=create-next-app&utm_medium=appdir-template-tw&utm_campaign=create-next-app"
            target="_blank"
            rel="noopener noreferrer"
          >
            Documentation
          </a>
        </div>

        <div className="flex flex-row gap-8 row-start-2 justify-center items-center w-full">
          <div className="bg-white dark:bg-gray-900 p-6 rounded-lg shadow-md w-[40vw]">
            <h2 className="text-2xl font-bold mb-4 text-gray-900 dark:text-gray-100">Login To LinkedIn</h2>
            <form action="#" method="POST">
              <label htmlFor="email" className="block text-sm font-medium text-gray-700 dark:text-gray-300">Email:</label>
              <input 
                type="email" 
                id="email" 
                name="email" 
                required 
                className="w-full p-2 mt-1 border border-gray-300 dark:border-gray-600 rounded-md bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-gray-100"
              />

              <label htmlFor="password" className="block mt-3 text-sm font-medium text-gray-700 dark:text-gray-300">Password:</label>
              <input 
                type="password" 
                id="password" 
                name="password" 
                required 
                className="w-full p-2 mt-1 border border-gray-300 dark:border-gray-600 rounded-md bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-gray-100"
              />

              <button 
                type="submit" 
                className="w-full mt-4 p-2 bg-green-600 text-white rounded-md hover:bg-green-700 dark:bg-green-500 dark:hover:bg-green-400"
              >
                Login
              </button>
            </form>
          </div>
        </div>
      </main>

      <footer className="row-start-3 flex gap-6 flex-wrap items-center justify-center">
        <a
          className="flex items-center gap-2 hover:underline hover:underline-offset-4"
          href="https://nextjs.org/learn?utm_source=create-next-app&utm_medium=appdir-template-tw&utm_campaign=create-next-app"
          target="_blank"
          rel="noopener noreferrer"
        >
          <Image
            aria-hidden
            src="/file.svg"
            alt="File icon"
            width={16}
            height={16}
          />
          Learn
        </a>
        <a
          className="flex items-center gap-2 hover:underline hover:underline-offset-4"
          href="https://vercel.com/templates?framework=next.js&utm_source=create-next-app&utm_medium=appdir-template-tw&utm_campaign=create-next-app"
          target="_blank"
          rel="noopener noreferrer"
        >
          <Image
            aria-hidden
            src="/window.svg"
            alt="Window icon"
            width={16}
            height={16}
          />
          Examples
        </a>
        <a
          className="flex items-center gap-2 hover:underline hover:underline-offset-4"
          href="https://nextjs.org?utm_source=create-next-app&utm_medium=appdir-template-tw&utm_campaign=create-next-app"
          target="_blank"
          rel="noopener noreferrer"
        >
          <Image
            aria-hidden
            src="/globe.svg"
            alt="Globe icon"
            width={16}
            height={16}
          />
          Go to nextjs.org →
        </a>
      </footer>
    </div>
  );
}