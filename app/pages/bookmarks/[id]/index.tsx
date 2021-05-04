import React, { useEffect, useState } from 'react'
import Link from 'next/link'
import { useRouter } from 'next/router'
import styles from '../../../styles/Home.module.css'
import { OgpBox } from '../../../components/OgpBox'
import { getBookmarkByIdAsync } from '../../../lib/index'

export default function Details() {
  const router = useRouter()
  const { id } = router.query

  const [bookmark, setBookmark] = useState<any>(undefined);
  const [relatedBookmark, setRelated] = useState<Array<any>>([]);
  const [isLoading, setLoading] = useState<boolean>(true);

  useEffect(() => {
    if(!Number(id)) return
    const f = async () => {
      const res = await getBookmarkByIdAsync(Number(id));
      setBookmark(res.bookmark)
      setRelated(res.related)
      setLoading(false)
    }
    f();
  }, [id])

  const RelatedBookmarkList = relatedBookmark.map((item: any) => {
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
      <main className={styles.container}>
        <p>詳細</p>
        {
          isLoading?
          null :
          <div className={styles.content}>
            <OgpBox ogp={bookmark.ogp} />
            <p>[memo]</p>
            <p>{bookmark.memo}</p>
            <hr />
            {RelatedBookmarkList}
          </div>
        }
      </main>
    </div>
  )
}
