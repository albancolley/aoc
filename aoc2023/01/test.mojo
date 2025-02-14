from collections.vector import DynamicVector

fn main():
    
    # let list: ListLiteral[StringLiteral,StringLiteral,StringLiteral,StringLiteral,StringLiteral,StringLiteral,StringLiteral,StringLiteral,StringLiteral] = ["1", "2" ,"3" ,"4" ,"5" ,"6" ,"7" ,"8" ,"9"]
    # var list = ["1", "2" ,"3" ,"4" ,"5" ,"6" ,"7" ,"8" ,"9"]
    
    let s: String = "hello world"

    # print(list.get[2, StringLiteral]())
    for i in range(0, s.__len__()):
        print(s[i])

    var v: DynamicVector[Tuple[Int,Int]] = DynamicVector[Tuple[Int,Int]]()

    v.append((1,1))

    let a: Int = v[0].get[0,Int]()

    print(a)