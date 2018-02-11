@RestController
class HelloWorld{
  @RequestMapping("/")
  def sayhello(){
    return "hello liumiaocn"
  }
}