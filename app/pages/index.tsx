import Head from 'next/head'
import Link from 'next/link'
import React, { useCallback, useEffect, useState } from 'react';
import styles from '../styles/Home.module.css'
import axios from 'axios'
import { OgpBox } from '../components/OgpBox'
import { getAllBookmarksAsync, getOGP } from '../lib/index'

const BASE_URL = process.env.API_URL || 'http://localhost:5000'

interface IFormData {
  url: string,
  memo?: string,
  ogp: Object,
}

async function handleSubmit(formData: IFormData) {
  return axios.post(`${BASE_URL}/bookmarks`, formData)
    .then((res) => console.log(res.data))
    .catch((err) => console.log(err))
}

export default function Home() {

  const [url, setUrl] = useState<string>('');
  const [memo, setMemo] = useState<string>('');
  const [ogp, setOgp] = useState<Object>({});
  const [bookmarks, setBookmarks] = useState<Array<Object>>([]);

  const onChangeInputUrl = useCallback((event: React.ChangeEvent<HTMLInputElement>) => {
    setUrl(event.target.value);
  }, [])

  const onChangeInputMemo = useCallback((event: React.ChangeEvent<HTMLTextAreaElement>) => {
    setMemo(event.target.value);
  }, [])

  useEffect(() => {
    const f = async () => {
      const bookmarks = await getAllBookmarksAsync();
      setBookmarks(bookmarks)
    }
    f();
  }, [])

  const getOgpContent = useCallback(async () => {
      const ogpObject = await getOGP(url);
      console.log('[debug]', ogpObject);
      if(ogpObject[url] !== undefined && ogpObject !== {}) {
        setOgp(ogpObject[url])
      } else {
        setOgp({})
      }
  }, [ogp])

  const BookmarkList = bookmarks.map((item: any) => {
    return item.ogp.hasOwnProperty('og:title')?
    (<Link href="/bookmarks/[id]" as={`/bookmarks/${item.id}`} key={item.id}>
      <a>
        <OgpBox ogp={item.ogp} />
      </a>
    </Link>)
    : null
  })

  return (
    <div>
      <Head>
        <title>Create Next App</title>
        <meta name="description" content="Generated by create next app" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main className={styles.container}>
        <h1 className={styles.title}>栞 - Shiori -</h1>
        <div className={styles.content}>
          <input
            className={styles.formItem}
            value={url}
            onChange={onChangeInputUrl}
            placeholder="ブックマークするページのURL"
            onBlur={() => getOgpContent()}
          />
            {ogp.hasOwnProperty('og:title') ?
            <OgpBox ogp={ogp} /> : null}
          <textarea
            className={styles.formItem}
            value={memo}
            onChange={onChangeInputMemo}
            placeholder="メモ"
          />
          <button
            className={`${styles.formItem} btn`}
            type="button"
            onClick={() => handleSubmit({
              url: url,
              memo: memo,
              ogp: ogp
            })}
          >ブックマーク</button>
          <hr/>
          <p>ブックマーク一覧</p>
          {BookmarkList}
        </div>
      </main>

      <footer className={styles.footer}>
        wf-yamaday
      </footer>
    </div>
  )
}
