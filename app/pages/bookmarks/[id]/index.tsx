import React, { useEffect, useState } from 'react'
import { useRouter } from 'next/router'
import styles from '../../../styles/Home.module.css'
import { OgpBox } from '../../../components/OgpBox'
import { getBookmarkByIdAsync } from '../../../lib/index'

export default function Details() {
  const router = useRouter()
  const { id } = router.query

  const [bookmark, setBookmark] = useState<any>(undefined);

  useEffect(() => {
    if(!Number(id)) return
    const f = async () => {
      const bookmark = await getBookmarkByIdAsync(Number(id));
      setBookmark(bookmark)
    }
    f();
  })

  return (
    <div>
      <main className={styles.container}>
        <p>詳細</p>
        {
          bookmark?
          <div className={styles.content}>
            <OgpBox ogp={bookmark.ogp} />
            <p>memo</p>
            <p>{bookmark.memo}</p>
          </div>
          : null
        }
      </main>
    </div>
  )
}
